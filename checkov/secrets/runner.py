from __future__ import annotations

import datetime
import linecache
import logging
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING, cast, Optional, Iterable, Any, List

import requests

from checkov.common.util.decorators import time_it
from checkov.common.util.type_forcers import convert_str_to_bool

from checkov.common.bridgecrew.platform_integration import bc_integration
from checkov.common.output.secrets_record import SecretsRecord
from checkov.common.util.http_utils import request_wrapper
from detect_secrets import SecretsCollection
from detect_secrets.core import scan
from detect_secrets.settings import transient_settings

from checkov.common.bridgecrew.check_type import CheckType
from checkov.common.bridgecrew.integration_features.features.policy_metadata_integration import \
    integration as metadata_integration
from checkov.common.bridgecrew.severities import Severity
from checkov.common.comment.enum import COMMENT_REGEX
from checkov.common.models.consts import SUPPORTED_FILE_EXTENSIONS
from checkov.common.models.enums import CheckResult
from checkov.common.output.report import Report
from checkov.common.parallelizer.parallel_runner import parallel_runner
from checkov.common.runners.base_runner import BaseRunner, filter_ignored_paths
from checkov.common.runners.base_runner import ignored_directories
from checkov.common.typing import _CheckResult
from checkov.common.util.consts import DEFAULT_EXTERNAL_MODULES_DIR
from checkov.common.util.dockerfile import is_docker_file
from checkov.common.util.secrets import omit_secret_value_from_line
from checkov.runner_filter import RunnerFilter
from checkov.secrets.consts import ValidationStatus, VerifySecretsResult
from checkov.secrets.coordinator import EnrichedSecret, SecretsCoordinator
from checkov.secrets.plugins.load_detectors import get_runnable_plugins

if TYPE_CHECKING:
    from checkov.common.util.tqdm_utils import ProgressBar
    from detect_secrets.core.potential_secret import PotentialSecret

SOURCE_CODE_EXTENSION = ['.py', '.js', '.properties', '.pem', '.php', '.xml', '.ts', '.env', '.java', '.rb',
                         'go', 'cs', '.txt']
SECRET_TYPE_TO_ID = {
    'Artifactory Credentials': 'CKV_SECRET_1',
    'AWS Access Key': 'CKV_SECRET_2',
    'Azure Storage Account access key': 'CKV_SECRET_3',
    'Basic Auth Credentials': 'CKV_SECRET_4',
    'Cloudant Credentials': 'CKV_SECRET_5',
    'Base64 High Entropy String': 'CKV_SECRET_6',
    'Random High Entropy String': 'CKV_SECRET_78',
    'IBM Cloud IAM Key': 'CKV_SECRET_7',
    'IBM COS HMAC Credentials': 'CKV_SECRET_8',
    'JSON Web Token': 'CKV_SECRET_9',
    'Secret Keyword': 'CKV_SECRET_10',
    'Mailchimp Access Key': 'CKV_SECRET_11',
    'NPM tokens': 'CKV_SECRET_12',
    'Private Key': 'CKV_SECRET_13',
    'Slack Token': 'CKV_SECRET_14',
    'SoftLayer Credentials': 'CKV_SECRET_15',
    'Square OAuth Secret': 'CKV_SECRET_16',
    'Stripe Access Key': 'CKV_SECRET_17',
    'Twilio API Key': 'CKV_SECRET_18',
    'Hex High Entropy String': 'CKV_SECRET_19'
}
CHECK_ID_TO_SECRET_TYPE = {v: k for k, v in SECRET_TYPE_TO_ID.items()}

PROHIBITED_FILES = ['Pipfile.lock', 'yarn.lock', 'package-lock.json', 'requirements.txt']

MAX_FILE_SIZE = int(os.getenv('CHECKOV_MAX_FILE_SIZE', '5000000'))  # 5 MB is default limit


class Runner(BaseRunner[None]):
    check_type = CheckType.SECRETS  # noqa: CCE003  # a static attribute

    def __init__(self, file_extensions: Iterable[str] | None = None, file_names: Iterable[str] | None = None):
        super().__init__(file_extensions, file_names)
        self.secrets_coordinator = SecretsCoordinator()

    def run(
            self,
            root_folder: str | None,
            external_checks_dir: list[str] | None = None,
            files: list[str] | None = None,
            runner_filter: RunnerFilter | None = None,
            collect_skip_comments: bool = True
    ) -> Report:
        runner_filter = runner_filter or RunnerFilter()
        current_dir = Path(__file__).parent
        secrets = SecretsCollection()
        plugins_used = [
            {'name': 'AWSKeyDetector'},
            {'name': 'ArtifactoryDetector'},
            {'name': 'AzureStorageKeyDetector'},
            {'name': 'BasicAuthDetector'},
            {'name': 'CloudantDetector'},
            {'name': 'IbmCloudIamDetector'},
            {'name': 'MailchimpDetector'},
            {'name': 'PrivateKeyDetector'},
            {'name': 'SlackDetector'},
            {'name': 'SoftlayerDetector'},
            {'name': 'SquareOAuthDetector'},
            {'name': 'StripeDetector'},
            {'name': 'TwilioKeyDetector'},
            {'name': 'EntropyKeywordCombinator', 'path': f'file://{current_dir}/plugins/entropy_keyword_combinator.py'}
        ]

        # load runnable plugins
        customer_run_config = bc_integration.customer_run_config_response
        plugins_index = 0
        if customer_run_config:
            policies_list = customer_run_config.get('secretsPolicies', [])
            if policies_list:
                runnable_plugins: dict[str, str] = get_runnable_plugins(policies_list)
                logging.info(f"Found {len(runnable_plugins)} runnable plugins")
                if len(runnable_plugins) > 0:
                    plugins_index += 1
                for name, runnable_plugin in runnable_plugins.items():
                    f = open(f"runnable_plugin_{plugins_index}.py", "w")
                    f.write(runnable_plugin)
                    f.close()
                    plugins_used.append({
                        'name': name.replace(' ', ''),
                        'path': f'file://runnable_plugin_{plugins_index}.py'
                    })
                    plugins_index += 1
                    logging.info(f"Loaded runnable plugin {name}")
        # load internal regex detectors
        detector_path = f"{current_dir}/plugins/custom_regex_detector.py"
        logging.info(f"Custom detector found at {detector_path}. Loading...")
        plugins_used.append({
            'name': 'CustomRegexDetector',
            'path': f'file://{detector_path}'
        })
        with transient_settings({
            # Only run scans with only these plugins.
            'plugins_used': plugins_used
        }) as settings:
            report = Report(self.check_type)
            if not runner_filter.show_progress_bar:
                self.pbar.turn_off_progress_bar()

            # Implement non IaC files (including .terraform dir)
            files_to_scan = files or []
            excluded_paths = (runner_filter.excluded_paths or []) + ignored_directories + [DEFAULT_EXTERNAL_MODULES_DIR]
            if root_folder:
                enable_secret_scan_all_files = runner_filter.enable_secret_scan_all_files
                block_list_secret_scan = runner_filter.block_list_secret_scan or []
                block_list_secret_scan_lower = [file_type.lower() for file_type in block_list_secret_scan]
                for root, d_names, f_names in os.walk(root_folder):
                    filter_ignored_paths(root, d_names, excluded_paths)
                    filter_ignored_paths(root, f_names, excluded_paths)
                    for file in f_names:
                        if enable_secret_scan_all_files:
                            if is_docker_file(file):
                                if 'dockerfile' not in block_list_secret_scan_lower:
                                    files_to_scan.append(os.path.join(root, file))
                            elif f".{file.split('.')[-1]}" not in block_list_secret_scan_lower:
                                files_to_scan.append(os.path.join(root, file))
                        elif file not in PROHIBITED_FILES and f".{file.split('.')[-1]}" in SUPPORTED_FILE_EXTENSIONS or is_docker_file(
                                file):
                            files_to_scan.append(os.path.join(root, file))
            logging.info(f'Secrets scanning will scan {len(files_to_scan)} files')

            settings.disable_filters(*['detect_secrets.filters.heuristic.is_indirect_reference'])

            self.pbar.initiate(len(files_to_scan))
            self._scan_files(files_to_scan, secrets, self.pbar)
            self.pbar.close()
            secrets_duplication: dict[str, bool] = {}
            self._add_custom_detectors_to_metadata_integration()
            for _, secret in secrets:
                check_id = getattr(secret, "check_id", SECRET_TYPE_TO_ID.get(secret.type))
                if not check_id:
                    logging.debug(f'Secret was filtered - no check_id for line_number {secret.line_number}')
                    continue
                secret_key = f'{secret.filename}_{secret.line_number}_{secret.secret_hash}'
                if secret_key in secrets_duplication:
                    logging.debug(f'Secret was filtered - secrets_duplication. line_number {secret.line_number}, check_id {check_id}')
                    continue
                else:
                    secrets_duplication[secret_key] = True
                bc_check_id = metadata_integration.get_bc_id(check_id)
                severity = metadata_integration.get_severity(check_id)
                if not runner_filter.should_run_check(check_id=check_id, bc_check_id=bc_check_id, severity=severity,
                                                      report_type=CheckType.SECRETS):
                    logging.debug(
                        f'Check was suppress - should_run_check. check_id {check_id}')
                    continue
                result: _CheckResult = {'result': CheckResult.FAILED}
                try:
                    line_text = linecache.getline(secret.filename, secret.line_number)
                except SyntaxError as e:
                    # If encoding is a problem, this is probably not human-readable source code
                    # hence there's no need in flagging this secret
                    logging.info(f'Failed to log secret {secret.type} for file {secret.filename} because of {e}')
                    continue
                if line_text and line_text.startswith('git_commit'):
                    continue
                result = self.search_for_suppression(
                    check_id=check_id,
                    bc_check_id=bc_check_id,
                    severity=severity,
                    secret=secret,
                    runner_filter=runner_filter,
                    root_folder=root_folder
                ) or result
                relative_file_path = f'/{os.path.relpath(secret.filename, root_folder)}'
                resource = f'{relative_file_path}:{secret.secret_hash}'
                report.add_resource(resource)
                # 'secret.secret_value' can actually be 'None', but only when 'PotentialSecret' was created
                # via 'load_secret_from_dict'
                self.save_secret_to_coordinator(secret.secret_value, bc_check_id, resource, result)
                line_text_censored = omit_secret_value_from_line(cast(str, secret.secret_value), line_text)
                report.add_record(SecretsRecord(
                    check_id=check_id,
                    bc_check_id=bc_check_id,
                    severity=severity,
                    check_name=secret.type,
                    check_result=result,
                    code_block=[(secret.line_number, line_text_censored)],
                    file_path=relative_file_path,
                    file_line_range=[secret.line_number, secret.line_number + 1],
                    resource=secret.secret_hash,
                    check_class="",
                    evaluations=None,
                    file_abs_path=os.path.abspath(secret.filename),
                    validation_status=ValidationStatus.UNAVAILABLE.value
                ))

            enriched_secrets_s3_path = bc_integration.persist_enriched_secrets(self.secrets_coordinator.get_secrets())
            if enriched_secrets_s3_path:
                self.verify_secrets(report, enriched_secrets_s3_path)
            logging.debug(f'report fail checks len: {len(report.failed_checks)}')

            self.cleanup_plugin_files(plugins_index)
            if runner_filter.skip_invalid_secrets:
                self._modify_invalid_secrets_check_result_to_skipped(report)
            return report

    def cleanup_plugin_files(self, amount: int) -> None:
        for index in range(1, amount):
            try:
                os.remove(f"runnable_plugin_{index}.py")
                logging.info(f"Removed runnable plugin at index {index}")
            except Exception as e:
                logging.info(f"Failed removing file at index {index} due to: {e}")

    @staticmethod
    def _scan_files(files_to_scan: list[str], secrets: SecretsCollection, pbar: ProgressBar) -> None:
        # implemented the scan function like secrets.scan_files
        base_path = secrets.root
        results = parallel_runner.run_function(
            func=lambda f: Runner._safe_scan(f, base_path),
            items=files_to_scan,
            run_multiprocess=os.getenv("RUN_SECRETS_MULTIPROCESS", "").lower() == "true"
        )

        for filename, secrets_results in results:
            pbar.set_additional_data({'Current File Scanned': str(filename)})
            for secret in secrets_results:
                secrets[os.path.relpath(secret.filename, base_path)].add(secret)
            pbar.update()

    @staticmethod
    def _safe_scan(file_path: str, base_path: str) -> tuple[str, list[PotentialSecret]]:
        full_file_path = os.path.join(base_path, file_path)
        file_size = os.path.getsize(full_file_path)
        if file_size > MAX_FILE_SIZE > 0:
            logging.info(
                f'Skipping secret scanning on {full_file_path} due to file size. To scan this file for '
                'secrets, run this command again with the environment variable "CHECKOV_MAX_FILE_SIZE" '
                f'to 0 or {file_size + 1}'
            )
            return file_path, []
        try:
            start_time = datetime.datetime.now()
            file_results = [*scan.scan_file(full_file_path)]
            logging.info(f'file {full_file_path} results len {len(file_results)}')
            end_time = datetime.datetime.now()
            run_time = end_time - start_time
            if run_time > datetime.timedelta(seconds=10):
                logging.info(f'Secret scanning for {full_file_path} took {run_time} seconds')
            return file_path, file_results
        except Exception as e:
            logging.warning(f"Secret scanning: could not process file {full_file_path}")
            logging.debug(e, exc_info=True)
            return file_path, []

    @staticmethod
    def search_for_suppression(
            check_id: str,
            bc_check_id: str,
            severity: Severity | None,
            secret: PotentialSecret,
            runner_filter: RunnerFilter,
            root_folder: str | None
    ) -> _CheckResult | None:
        if not runner_filter.should_run_check(
                check_id=check_id,
                bc_check_id=bc_check_id,
                severity=severity,
                report_type=CheckType.SECRETS,
                file_origin_paths=[secret.filename],
                root_folder=root_folder
        ) and check_id in CHECK_ID_TO_SECRET_TYPE.keys():
            return {
                "result": CheckResult.SKIPPED,
                "suppress_comment": f"Secret scan {check_id} is skipped"
            }

        # Check for suppression comment in the line before, the line of, and the line after the secret
        for line_number in [secret.line_number, secret.line_number - 1, secret.line_number + 1]:
            lt = linecache.getline(secret.filename, line_number)
            skip_search = re.search(COMMENT_REGEX, lt)
            if skip_search and (skip_search.group(2) == check_id or skip_search.group(2) == bc_check_id):
                return {
                    "result": CheckResult.SKIPPED,
                    "suppress_comment": skip_search.group(3)[1:] if skip_search.group(3) else "No comment provided"
                }
        return None

    def save_secret_to_coordinator(self, secret_value: Optional[str], bc_check_id: str, resource: str,
                                   result: _CheckResult) \
            -> None:
        if result.get('result') == CheckResult.FAILED and secret_value is not None:
            enriched_secret = EnrichedSecret(original_secret=secret_value, bc_check_id=bc_check_id, resource=resource)
            self.secrets_coordinator.add_secret(enriched_secret=enriched_secret)

    @time_it
    def verify_secrets(self, report: Report, enriched_secrets_s3_path: str) -> VerifySecretsResult:
        if not bc_integration.bc_api_key or not convert_str_to_bool(os.getenv("CKV_VALIDATE_SECRETS", False)):
            logging.debug(
                'Secrets verification is off, enabled it via env var CKV_VALIDATE_SECRETS and provide an api key')
            return VerifySecretsResult.INSUFFICIENT_PARAMS

        if bc_integration.skip_download:
            logging.debug('Skipping secrets verification as flag skip-download was specified')
            return VerifySecretsResult.INSUFFICIENT_PARAMS

        request_body = {
            "reportS3Path": enriched_secrets_s3_path
        }
        response = None
        try:
            response = request_wrapper(
                "POST", f"{bc_integration.api_url}/api/v1/secrets/reportVerification",
                headers=bc_integration.get_default_headers("POST"),
                json=request_body,
                should_call_raise_for_status=True,
                log_json_body=False
            )
        except Exception:
            logging.error('Failed to perform secrets verification', exc_info=True)

        if not response:
            return VerifySecretsResult.FAILURE

        verification_report_presigned_url = response.json().get('verificationReportSignedUrl')
        if not verification_report_presigned_url:
            logging.error("Response is missing verificationReportSignedUrl key, aborting")
            return VerifySecretsResult.FAILURE

        verification_report = self.get_json_verification_report(verification_report_presigned_url)

        if not verification_report:
            return VerifySecretsResult.FAILURE

        validation_status_by_check_id_and_resource = {}
        for validation_status_entity in verification_report:
            if not all(required_key in validation_status_entity.keys() for required_key in ["violationId", "resourceId", "status"]):
                logging.debug(f"{validation_status_entity} does not have all required keys, skipping")
                continue

            key = f'{validation_status_entity["violationId"]}_{validation_status_entity["resourceId"]}'
            validation_status_by_check_id_and_resource[key] = validation_status_entity['status']

        logging.debug(f'secrets verification api returned with {len(validation_status_by_check_id_and_resource.keys())} unique entries')

        for secrets_record in report.failed_checks:
            if hasattr(secrets_record, "validation_status"):
                key = f'{secrets_record.bc_check_id}_{secrets_record.file_path}:{secrets_record.resource}'
                secrets_record.validation_status = validation_status_by_check_id_and_resource.get(key)

                if secrets_record.validation_status is None:
                    logging.debug(f'Failed to find verification status of {key}, setting by default to Unknown')
                    secrets_record.validation_status = ValidationStatus.UNAVAILABLE.value

        return VerifySecretsResult.SUCCESS

    @staticmethod
    def get_json_verification_report(presigned_url: str) -> list[dict[str, str]] | None:
        response = None
        try:
            response = requests.get(presigned_url)
        except Exception:
            logging.error('Unable to download verification report')

        return response.json() if response else None

    @staticmethod
    def _add_custom_detectors_to_metadata_integration() -> None:
        customer_run_config_response = bc_integration.customer_run_config_response
        policies_list: List[dict[str, Any]] = []
        if customer_run_config_response:
            policies_list = customer_run_config_response.get('secretsPolicies', [])
        for policy in policies_list:
            if policy.get('isCustom', False):
                check_id = policy['incidentId']
                guideline = policy.get('guideline', '')
                severity = policy.get('severity', '')
                metadata_integration.check_metadata[check_id] = {'id': check_id,
                                                                 'guideline': guideline,
                                                                 'severity': severity}

    @staticmethod
    def _modify_invalid_secrets_check_result_to_skipped(report: Report) -> None:
        checks_indexes_moved_to_skipped: list[int] = []

        for check_index, check in enumerate(report.failed_checks):
            if hasattr(check, 'validation_status') and check.validation_status == ValidationStatus.INVALID.value:
                check.check_result["result"] = CheckResult.SKIPPED
                check.check_result["suppress_comment"] = "Skipped invalid secret"
                report.skipped_checks.append(check)
                checks_indexes_moved_to_skipped.append(check_index)

        for idx in sorted(checks_indexes_moved_to_skipped, reverse=True):
            try:
                del report.failed_checks[idx]
            except Exception:
                logging.error(f"Failed to remove suppressed secrets violations from failed_checks, report is corrupted."
                              f"Tried to delete entry {idx} from failed_checks of length {len(report.failed_checks)}",
                              exc_info=True)

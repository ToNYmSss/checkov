---
layout: default
title: github_actions resource scans
nav_order: 1
---

# github_actions resource scans (auto generated)

|    | Id         | Type     | Entity         | Policy                                                                                                                                                                            | IaC            | Resource Link                                                                                                                 |
|----|------------|----------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------|
|  0 | CKV_GHA_1  | jobs     | jobs           | Ensure ACTIONS_ALLOW_UNSECURE_COMMANDS isn't true on environment variables                                                                                                        | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/AllowUnsecureCommandsOnJob.py             |
|  1 | CKV_GHA_1  | jobs     | jobs.*.steps[] | Ensure ACTIONS_ALLOW_UNSECURE_COMMANDS isn't true on environment variables                                                                                                        | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/AllowUnsecureCommandsOnJob.py             |
|  2 | CKV_GHA_2  | jobs     | jobs           | Ensure run commands are not vulnerable to shell injection                                                                                                                         | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/ShellInjection.py                         |
|  3 | CKV_GHA_2  | jobs     | jobs.*.steps[] | Ensure run commands are not vulnerable to shell injection                                                                                                                         | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/ShellInjection.py                         |
|  4 | CKV_GHA_3  | jobs     | jobs           | Suspicious use of curl with secrets                                                                                                                                               | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/SuspectCurlInScript.py                    |
|  5 | CKV_GHA_3  | jobs     | jobs.*.steps[] | Suspicious use of curl with secrets                                                                                                                                               | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/SuspectCurlInScript.py                    |
|  6 | CKV_GHA_4  | jobs     | jobs           | Suspicious use of netcat with IP address                                                                                                                                          | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/ReverseShellNetcat.py                     |
|  7 | CKV_GHA_4  | jobs     | jobs.*.steps[] | Suspicious use of netcat with IP address                                                                                                                                          | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/ReverseShellNetcat.py                     |
|  8 | CKV_GHA_5  | jobs     | jobs           | Found artifact build without evidence of cosign sign execution in pipeline                                                                                                        | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/CosignArtifacts.py                        |
|  9 | CKV_GHA_6  | jobs     | jobs           | Found artifact build without evidence of cosign sbom attestation in pipeline                                                                                                      | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/CosignSBOM.py                             |
| 10 | CKV_GHA_7  | jobs     | on             | The build output cannot be affected by user parameters other than the build entry point and the top-level source location. GitHub Actions workflow_dispatch inputs MUST be empty. | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/job/EmptyWorkflowDispatch.py                  |
| 11 | CKV2_GHA_1 | resource | permissions    | Ensure top-level permissions are not set to write-all                                                                                                                             | github_actions | https://github.com/bridgecrewio/checkov/blob/main/checkov/github_actions/checks/graph_checks/ReadOnlyTopLevelPermissions.yaml |


---



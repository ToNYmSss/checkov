# CHANGELOG

## [Unreleased](https://github.com/bridgecrewio/checkov/compare/2.2.320...HEAD)

## [2.2.320](https://github.com/bridgecrewio/checkov/compare/2.2.316...2.2.320) - 2023-01-31

### Feature

- **sca:** Add a --support flag - [#4323](https://github.com/bridgecrewio/checkov/pull/4323)
- **sca:** added extra supported package files to find_scannable_files - [#4378](https://github.com/bridgecrewio/checkov/pull/4378)
- **terraform:** add reset edges function to terraform local graph - [#4373](https://github.com/bridgecrewio/checkov/pull/4373)
- **terraform:** Added base class for cloudsplaining iam checks to be integrated between data and resource objects - [#4338](https://github.com/bridgecrewio/checkov/pull/4338)
- **terraform:** Added basic check with test for tf resource with IAM privilege escalation - [#4376](https://github.com/bridgecrewio/checkov/pull/4376)

### Bug Fix

- **cloudformation:** Skip SAM Global Tags propagation - [#4383](https://github.com/bridgecrewio/checkov/pull/4383)
- **sca:** extend image name validation - [#4377](https://github.com/bridgecrewio/checkov/pull/4377)
- **terraform:** simple check naming fix - [#4371](https://github.com/bridgecrewio/checkov/pull/4371)

## [2.2.316](https://github.com/bridgecrewio/checkov/compare/2.2.312...2.2.316) - 2023-01-30

### Feature

- **sca:** ignore package.json file when yarn.lock exists - [#4370](https://github.com/bridgecrewio/checkov/pull/4370)
- **terraform:** GCP check kms policy does not define public access - [#4190](https://github.com/bridgecrewio/checkov/pull/4190)
- **terraform:** GCP check policy isn't public - [#4194](https://github.com/bridgecrewio/checkov/pull/4194)

### Bug Fix

- **sca:** support BC_VUL_X IDs in GitLab SAST output - [#4360](https://github.com/bridgecrewio/checkov/pull/4360)

## [2.2.312](https://github.com/bridgecrewio/checkov/compare/2.2.305...2.2.312) - 2023-01-29

### Feature

- **azure:** fix container latest tag missing results - [#4337](https://github.com/bridgecrewio/checkov/pull/4337)

### Bug Fix

- **azure:** Add `.*.` in azure checks to check in lists as well - [#4355](https://github.com/bridgecrewio/checkov/pull/4355)
- **azure:** Azure checks fixes - [#4342](https://github.com/bridgecrewio/checkov/pull/4342)
- **azure:** Azure checks fixes - [#4354](https://github.com/bridgecrewio/checkov/pull/4354)
- **azure:** Support string function_app min_tls_version as well - [#4357](https://github.com/bridgecrewio/checkov/pull/4357)
- **kubernetes:** k8s checks fixes - [#4343](https://github.com/bridgecrewio/checkov/pull/4343)
- **sca:** Fix multiple issues related to IR - [#4358](https://github.com/bridgecrewio/checkov/pull/4358)
- **terraform:** Terraform checks fixes - [#4344](https://github.com/bridgecrewio/checkov/pull/4344)

## [2.2.305](https://github.com/bridgecrewio/checkov/compare/2.2.304...2.2.305) - 2023-01-28

### Feature

- **general:** Add GitLab SAST output - [#4315](https://github.com/bridgecrewio/checkov/pull/4315)

## [2.2.304](https://github.com/bridgecrewio/checkov/compare/2.2.302...2.2.304) - 2023-01-26

### Bug Fix

- **kubernetes:** skip extracting pods for custom resources - [#4334](https://github.com/bridgecrewio/checkov/pull/4334)
- **sca:** require requests 2.27.0 - [#4339](https://github.com/bridgecrewio/checkov/pull/4339)

### Documentation

- **general:** fix env var name to `CKV_IGNORE_HIDDEN_DIRECTORIES` - [#4335](https://github.com/bridgecrewio/checkov/pull/4335)

## [2.2.302](https://github.com/bridgecrewio/checkov/compare/2.2.299...2.2.302) - 2023-01-25

### Feature

- **general:** igraph library support - [#4327](https://github.com/bridgecrewio/checkov/pull/4327)

### Bug Fix

- **general:** add missing header in --list output - [#4329](https://github.com/bridgecrewio/checkov/pull/4329)
- **kubernetes:** extract pods only for supported resources - [#4330](https://github.com/bridgecrewio/checkov/pull/4330)
- **sca:** catch exceptional error during SCA results polling - [#4331](https://github.com/bridgecrewio/checkov/pull/4331)
- **terraform:** change terraform nested modules path separators - [#4319](https://github.com/bridgecrewio/checkov/pull/4319)
- **terraform:** handle unexpected container definition type - [#4328](https://github.com/bridgecrewio/checkov/pull/4328)

## [2.2.299](https://github.com/bridgecrewio/checkov/compare/2.2.292...2.2.299) - 2023-01-24

### Feature

- **azure:** change detect image source - [#4320](https://github.com/bridgecrewio/checkov/pull/4320)
- **general:** add empty azure image check - [#4308](https://github.com/bridgecrewio/checkov/pull/4308)
- **general:** add logs for async license and image retrieval  - [#4317](https://github.com/bridgecrewio/checkov/pull/4317)
- **sca:** Support the new --image flag along the --docker-image flag  - [#4314](https://github.com/bridgecrewio/checkov/pull/4314)

### Bug Fix

- **general:** ignore repo_id setting when list flag is set - [#4313](https://github.com/bridgecrewio/checkov/pull/4313)
- **kubernetes:** handle k8s resource with missing required data - [#4318](https://github.com/bridgecrewio/checkov/pull/4318)
- **secrets:** Change s3 path for enriched secrets upload - [#4275](https://github.com/bridgecrewio/checkov/pull/4275)
- **terraform:** handle unexpected container type - [#4311](https://github.com/bridgecrewio/checkov/pull/4311)

### Documentation

- **general:** Update README for supported Python versions - [#4305](https://github.com/bridgecrewio/checkov/pull/4305)

## [2.2.292](https://github.com/bridgecrewio/checkov/compare/2.2.289...2.2.292) - 2023-01-23

### Feature

- **terraform:** new app service checks for azurerm - [#4072](https://github.com/bridgecrewio/checkov/pull/4072)

### Bug Fix

- **general:** In case of a non-JSON response, log the response - [#4304](https://github.com/bridgecrewio/checkov/pull/4304)
- **terraform_plan:** fix in deep analysis - [#4306](https://github.com/bridgecrewio/checkov/pull/4306)
- **terraform:** fix default behaviour of CKV_GCP_19 - [#4289](https://github.com/bridgecrewio/checkov/pull/4289)

## [2.2.289](https://github.com/bridgecrewio/checkov/compare/2.2.281...2.2.289) - 2023-01-22

### Feature

- **general:** add Ansible framework - [#4244](https://github.com/bridgecrewio/checkov/pull/4244)
- **general:** Allow using `--repo-root-for-plan-enrichment` flag in GitHub Actions - [#4292](https://github.com/bridgecrewio/checkov/pull/4292)
- **secrets:** add new sanity test files for base64 entropy detector - [#4298](https://github.com/bridgecrewio/checkov/pull/4298)
- **terraform:** Adding yaml based build time policies for corresponding PC run time policies - [#4265](https://github.com/bridgecrewio/checkov/pull/4265)

### Bug Fix

- **sca:** fix dependency tree cli print - [#4282](https://github.com/bridgecrewio/checkov/pull/4282)
- **terraform:** fix Exception in image ref - [#4297](https://github.com/bridgecrewio/checkov/pull/4297)
- **terraform:** fix in variable rendering - [#4296](https://github.com/bridgecrewio/checkov/pull/4296)
- **terraform:** Fix policy str in graph checks - [#4286](https://github.com/bridgecrewio/checkov/pull/4286)

## [2.2.281](https://github.com/bridgecrewio/checkov/compare/2.2.278...2.2.281) - 2023-01-19

### Feature

- **general:** add Image referencer igraph support - [#4277](https://github.com/bridgecrewio/checkov/pull/4277)
- **general:** Support aiohttp for IR API calls - [#4274](https://github.com/bridgecrewio/checkov/pull/4274)

### Bug Fix

- **general:** Enable running cloned policies in case the OOTB policy is suppressed - [#4281](https://github.com/bridgecrewio/checkov/pull/4281)
- **secrets:** change default secret validation status to unavailable - [#4284](https://github.com/bridgecrewio/checkov/pull/4284)
- **terraform:** fix error for push_skipped_checks_down with definition that not in the definition context - [#4272](https://github.com/bridgecrewio/checkov/pull/4272)

## [2.2.278](https://github.com/bridgecrewio/checkov/compare/2.2.274...2.2.278) - 2023-01-18

### Feature

- **azure:** Add image referencer in azure pipelines - [#4234](https://github.com/bridgecrewio/checkov/pull/4234)
- **gha:** fix yaml parsing of multi files - [#4270](https://github.com/bridgecrewio/checkov/pull/4270)
- **secrets:** fix to keyword combinator to reduce FPs - [#4260](https://github.com/bridgecrewio/checkov/pull/4260)

### Bug Fix

- **secrets:** add guideline and severity to custom secret check metadata - [#4276](https://github.com/bridgecrewio/checkov/pull/4276)

## [2.2.274](https://github.com/bridgecrewio/checkov/compare/2.2.271...2.2.274) - 2023-01-17

### Feature

- **gha:** fix failing image retrieval in GHA IR - [#4268](https://github.com/bridgecrewio/checkov/pull/4268)

### Bug Fix

- **cloudformation:** fix CloudFormation checks related to number values - [#4243](https://github.com/bridgecrewio/checkov/pull/4243)
- **general:** Add normalization to change the name of nuget to dotNet lang - [#4271](https://github.com/bridgecrewio/checkov/pull/4271)

## [2.2.271](https://github.com/bridgecrewio/checkov/compare/2.2.264...2.2.271) - 2023-01-16

### Feature

- **dockerfile:** Add checks for PYTHONHTTPSVERIFY and NODE_TLS_REJECT_UNAUTHORIZED - [#4223](https://github.com/bridgecrewio/checkov/pull/4223)
- **secrets:** Skip invalid secrets checks + soft/hard fails - [#4247](https://github.com/bridgecrewio/checkov/pull/4247)
- **terraform:** Azure search service checks - [#4064](https://github.com/bridgecrewio/checkov/pull/4064)
- **terraform:** GCP checks for definition of a firewall resource for a network - [#4188](https://github.com/bridgecrewio/checkov/pull/4188)

### Bug Fix

- **general:** Support encoding of function object - [#4259](https://github.com/bridgecrewio/checkov/pull/4259)
- **kubernetes:** handle missing subjects in k8s cluster role binding - [#4262](https://github.com/bridgecrewio/checkov/pull/4262)
- **kubernetes:** handle resources with incompatible selector - [#4257](https://github.com/bridgecrewio/checkov/pull/4257)
- **secrets:** Change secret validation status message - [#4250](https://github.com/bridgecrewio/checkov/pull/4250)
- **terraform:** default value for CKV_AZURE_5 - [#4237](https://github.com/bridgecrewio/checkov/pull/4237)
- **terraform:** fix get_current_module_index for path that contain .tf in them - [#4261](https://github.com/bridgecrewio/checkov/pull/4261)

## [2.2.264](https://github.com/bridgecrewio/checkov/compare/2.2.258...2.2.264) - 2023-01-15

### Feature

- **general:** fix circleci crash when cannot find image - [#4249](https://github.com/bridgecrewio/checkov/pull/4249)
- **general:** fix circleci yaml-doc - [#4246](https://github.com/bridgecrewio/checkov/pull/4246)
- **kubernetes:** set default k8s graph env vars to true - [#4225](https://github.com/bridgecrewio/checkov/pull/4225)
- **terraform:** Add new checks for ensuring execution history logging and Xray for State Machine is enabled  - [#4240](https://github.com/bridgecrewio/checkov/pull/4240)

### Bug Fix

- **cloudformation:** Fix edge-cases in checks - [#4251](https://github.com/bridgecrewio/checkov/pull/4251)
- **kubernetes:** removed env vars from tests - [#4252](https://github.com/bridgecrewio/checkov/pull/4252)
- **secrets:** Change secret validation status message - [#4238](https://github.com/bridgecrewio/checkov/pull/4238)
- **secrets:** Revert "fix(secrets): Change secret validation status message" - [#4248](https://github.com/bridgecrewio/checkov/pull/4248)

## [2.2.258](https://github.com/bridgecrewio/checkov/compare/2.2.257...2.2.258) - 2023-01-12

### Feature

- **terraform:** PC-Policy-Team - GCP PostgreSQL Instance Database Policies - [#4090](https://github.com/bridgecrewio/checkov/pull/4090)

## [2.2.257](https://github.com/bridgecrewio/checkov/compare/2.2.254...2.2.257) - 2023-01-11

### Bug Fix

- **secrets:** Change verify secrets key to include relative path - [#4232](https://github.com/bridgecrewio/checkov/pull/4232)
- **terraform:** improve cross-variable edges performance - [#4231](https://github.com/bridgecrewio/checkov/pull/4231)

## [2.2.254](https://github.com/bridgecrewio/checkov/compare/2.2.252...2.2.254) - 2023-01-10

### Feature

- **general:** Add resource attributes to omit arg - [#4193](https://github.com/bridgecrewio/checkov/pull/4193)
- **terraform:** enable cross variable edges - [#4224](https://github.com/bridgecrewio/checkov/pull/4224)

### Bug Fix

- **secrets:** add function to add the custom policies to the metadata integration not in the multiprocess - [#4221](https://github.com/bridgecrewio/checkov/pull/4221)

## [2.2.252](https://github.com/bridgecrewio/checkov/compare/2.2.246...2.2.252) - 2023-01-09

### Feature

- **kubernetes:** support more types of k8s pod template containers - [#4208](https://github.com/bridgecrewio/checkov/pull/4208)
- **secrets:** Add secret validation status to reduced report - [#4219](https://github.com/bridgecrewio/checkov/pull/4219)
- **secrets:** fix unquoted secret value - [#4214](https://github.com/bridgecrewio/checkov/pull/4214)
- **terraform_plan:** support multiple references in one resource - [#4206](https://github.com/bridgecrewio/checkov/pull/4206)

### Bug Fix

- **kubernetes:** allow filtering of custom with built-in Kubernetes check IDs - [#4204](https://github.com/bridgecrewio/checkov/pull/4204)
- **secrets:** add long to see metadata_integration - [#4220](https://github.com/bridgecrewio/checkov/pull/4220)
- **terraform_plan:** fix module resources ids - [#4211](https://github.com/bridgecrewio/checkov/pull/4211)

## [2.2.246](https://github.com/bridgecrewio/checkov/compare/2.2.239...2.2.246) - 2023-01-08

### Feature

- **dockerfile:** Add checks for unsafe wget and pip usages - [#4202](https://github.com/bridgecrewio/checkov/pull/4202)
- **secrets:** Implement lower entropy threshold on a line with keyword - [#4210](https://github.com/bridgecrewio/checkov/pull/4210)
- **terraform:** add CKV2_AWS_51 to Ensure AWS Managed IAMFullAccess IAM policy is not used. - [#4174](https://github.com/bridgecrewio/checkov/pull/4174)
- **terraform:** CDN and service bus checks for azure - [#4059](https://github.com/bridgecrewio/checkov/pull/4059)

### Bug Fix

- **secrets:** add logs - [#4215](https://github.com/bridgecrewio/checkov/pull/4215)
- **secrets:** add logs to secrets - [#4213](https://github.com/bridgecrewio/checkov/pull/4213)
- **secrets:** Disable verify secrets if skip_download is specified - [#4209](https://github.com/bridgecrewio/checkov/pull/4209)
- **secrets:** fix relative file path in secrets saved to coordinator - [#4212](https://github.com/bridgecrewio/checkov/pull/4212)

## [2.2.239](https://github.com/bridgecrewio/checkov/compare/2.2.238...2.2.239) - 2023-01-06

### Bug Fix

- **general:** fix incorrect billing message when frameworks are removed from --framework list - [#4201](https://github.com/bridgecrewio/checkov/pull/4201)

## [2.2.238](https://github.com/bridgecrewio/checkov/compare/2.2.234...2.2.238) - 2023-01-05

### Feature

- **dockerfile:** Add check for unsafe curl usages - [#4186](https://github.com/bridgecrewio/checkov/pull/4186)
- **general:** add logic to vcs scanning to prevent empty repo collabs failing check - [#4199](https://github.com/bridgecrewio/checkov/pull/4199)
- **terraform:** Adding yaml based build time policies for corresponding PC run time policies - [#4113](https://github.com/bridgecrewio/checkov/pull/4113)

### Bug Fix

- **general:** handle variable dependent values in policy - [#4200](https://github.com/bridgecrewio/checkov/pull/4200)
- **secrets:** Fix api key condition in verify_secrets - [#4195](https://github.com/bridgecrewio/checkov/pull/4195)
- **secrets:** Remove raw string modifier from re.compile - [#4197](https://github.com/bridgecrewio/checkov/pull/4197)

## [2.2.234](https://github.com/bridgecrewio/checkov/compare/2.2.230...2.2.234) - 2023-01-04

### Feature

- **sca:** enable CHECKOV_RUN_SCA_PACKAGE_SCAN_V2 env var - [#4192](https://github.com/bridgecrewio/checkov/pull/4192)
- **secrets:** Call secrets verify API - [#4181](https://github.com/bridgecrewio/checkov/pull/4181)

### Bug Fix

- **general:** set newer jsonschema dependency bound-  solves #2227 - [#4183](https://github.com/bridgecrewio/checkov/pull/4183)
- **general:** Update exclude-patterns.txt - [#4187](https://github.com/bridgecrewio/checkov/pull/4187)

### Documentation

- **general:** fix links in contributing docs - [#4184](https://github.com/bridgecrewio/checkov/pull/4184)

## [2.2.230](https://github.com/bridgecrewio/checkov/compare/2.2.229...2.2.230) - 2023-01-03

### Feature

- **general:** Skip check in json file - [#4172](https://github.com/bridgecrewio/checkov/pull/4172)

## [2.2.229](https://github.com/bridgecrewio/checkov/compare/2.2.220...2.2.229) - 2023-01-01

### Feature

- **gha:** add support for gha existing graph - [#4175](https://github.com/bridgecrewio/checkov/pull/4175)
- **secrets:** change secretsCoordinator to dict format - [#4169](https://github.com/bridgecrewio/checkov/pull/4169)
- **terraform:** added aws_ssoadmin_managed_policy_attachment resource to CKV_AWS_274 - [#4173](https://github.com/bridgecrewio/checkov/pull/4173)

### Bug Fix

- **general:** add link to BaseGraphRegistry checks - [#4177](https://github.com/bridgecrewio/checkov/pull/4177)
- **general:** change CODE_LINK_BASE from master to main - [#4178](https://github.com/bridgecrewio/checkov/pull/4178)
- **kubernetes:** remove unneeded context check - [#4171](https://github.com/bridgecrewio/checkov/pull/4171)
- **kustomize:** fixed kustomize abs_file_path - [#4159](https://github.com/bridgecrewio/checkov/pull/4159)
- **terraform:** out of range error by checking if list is empty - [#4176](https://github.com/bridgecrewio/checkov/pull/4176)

## [2.2.220](https://github.com/bridgecrewio/checkov/compare/2.2.217...2.2.220) - 2022-12-29

### Feature

- **sca:** remove report_results from checkov, as it is not used at all - [#4161](https://github.com/bridgecrewio/checkov/pull/4161)

### Bug Fix

- **general:** fix f-string log message - [#4170](https://github.com/bridgecrewio/checkov/pull/4170)

### Documentation

- **general:** fix reference link in Contributing docs page - [#4164](https://github.com/bridgecrewio/checkov/pull/4164)

## [2.2.217](https://github.com/bridgecrewio/checkov/compare/2.2.212...2.2.217) - 2022-12-28

### Feature

- **general:** Make code blocks for json check results focused on the relevant part - [#4130](https://github.com/bridgecrewio/checkov/pull/4130)
- **openapi:** Add v2 openAPI new checks - [#4112](https://github.com/bridgecrewio/checkov/pull/4112)
- **terraform:** new azure storage checks - [#4021](https://github.com/bridgecrewio/checkov/pull/4021)

### Bug Fix

- **github:** Handle entity configurations of type list - [#4160](https://github.com/bridgecrewio/checkov/pull/4160)
- **sca:** Fix extra space in output of dependencies - [#4162](https://github.com/bridgecrewio/checkov/pull/4162)

## [2.2.212](https://github.com/bridgecrewio/checkov/compare/2.2.207...2.2.212) - 2022-12-27

### Feature

- **azure:** Add check - azure keyvalut public network access - [#4155](https://github.com/bridgecrewio/checkov/pull/4155)

### Bug Fix

- **terraform:** fix edge-case in CKV_AZURE_183 check - [#4154](https://github.com/bridgecrewio/checkov/pull/4154)
- **terraform:** fix graph checks nested modules - [#4157](https://github.com/bridgecrewio/checkov/pull/4157)
- **terraform:** fix or connection graph checks nested modules - [#4158](https://github.com/bridgecrewio/checkov/pull/4158)

## [2.2.207](https://github.com/bridgecrewio/checkov/compare/2.2.201...2.2.207) - 2022-12-26

### Feature

- **kubernetes:** Support graph edges for nested (related) Pod resources. - [#4100](https://github.com/bridgecrewio/checkov/pull/4100)
- **secrets:** Keep original secrets data in runtime for further validation - [#4144](https://github.com/bridgecrewio/checkov/pull/4144)
- **secrets:** Keep original secrets data in runtime for further validation - [#4149](https://github.com/bridgecrewio/checkov/pull/4149)

### Bug Fix

- **general:** fix excluded paths for path with special characters - [#4152](https://github.com/bridgecrewio/checkov/pull/4152)
- **terraform:** add test path to exclude-patterns - [#4150](https://github.com/bridgecrewio/checkov/pull/4150)
- **terraform:** fix edge-case in CKV_AZURE_37 check - [#4153](https://github.com/bridgecrewio/checkov/pull/4153)
- **terraform:** fix getting graph entity config in terraform runner - [#4146](https://github.com/bridgecrewio/checkov/pull/4146)
- **terraform:** remove redundant nested definitions - [#4147](https://github.com/bridgecrewio/checkov/pull/4147)

## [2.2.201](https://github.com/bridgecrewio/checkov/compare/2.2.199...2.2.201) - 2022-12-25

### Bug Fix

- **secrets:** add support to conditionQuery - [#4086](https://github.com/bridgecrewio/checkov/pull/4086)
- **terraform:** fix edge-case in CKV_AZURE_183 check - [#4145](https://github.com/bridgecrewio/checkov/pull/4145)

## [2.2.199](https://github.com/bridgecrewio/checkov/compare/2.2.191...2.2.199) - 2022-12-22

### Feature

- **gha:** support on directive in workflow files - [#4125](https://github.com/bridgecrewio/checkov/pull/4125)
- **sca:** run old package scanning for IDE scan  - [#4133](https://github.com/bridgecrewio/checkov/pull/4133)
- **secrets:** expose maximum 6 characters of secret values - [#4140](https://github.com/bridgecrewio/checkov/pull/4140)

### Bug Fix

- **circleci:** add resource to ir - [#4135](https://github.com/bridgecrewio/checkov/pull/4135)
- **general:** Reformat PR template - [#4139](https://github.com/bridgecrewio/checkov/pull/4139)
- **kubernetes:** move Kubernetes context error message - [#4132](https://github.com/bridgecrewio/checkov/pull/4132)
- **terraform:** add aws_transfer_server to CKV2_AWS_5 check - [#4137](https://github.com/bridgecrewio/checkov/pull/4137)
- **terraform:** Add some more supported keys to bigquery public acl check ignore list to avoid false positive - [#3969](https://github.com/bridgecrewio/checkov/pull/3969)
- **terraform:** fix azure network address invalid value - [#4131](https://github.com/bridgecrewio/checkov/pull/4131)

## [2.2.191](https://github.com/bridgecrewio/checkov/compare/2.2.186...2.2.191) - 2022-12-21

### Feature

- **general:** add the stack trace to the error message when caught by main.py - [#4121](https://github.com/bridgecrewio/checkov/pull/4121)
- **sca:** add GCP Terraform resources for Image Referencer - [#4094](https://github.com/bridgecrewio/checkov/pull/4094)
- **sca:** protecting checkov with try/catch wrapping - [#4104](https://github.com/bridgecrewio/checkov/pull/4104)

### Bug Fix

- **kubernetes:** removed obsolete error logging - [#4126](https://github.com/bridgecrewio/checkov/pull/4126)
- **terraform:** fix azure dns invalid ip - [#4128](https://github.com/bridgecrewio/checkov/pull/4128)

## [2.2.186](https://github.com/bridgecrewio/checkov/compare/2.2.180...2.2.186) - 2022-12-20

### Feature

- **general:** move the jsonpath try/catch up a level to catch more errors - [#3911](https://github.com/bridgecrewio/checkov/pull/3911)
- **sca:** returning exit code 2 in case of error for downloading twistcli - [#4105](https://github.com/bridgecrewio/checkov/pull/4105)

### Bug Fix

- **dockerfile:** adjust the file abs path for Dockerfile graph results - [#4118](https://github.com/bridgecrewio/checkov/pull/4118)
- **openapi:** fix an open API CKV_OPENAPI_6 check - [#4109](https://github.com/bridgecrewio/checkov/pull/4109)
- **sca:** fixing integration tests - [#4117](https://github.com/bridgecrewio/checkov/pull/4117)
- **terraform_plan:** use abs path for repo_root_for_plan_enrichment - [#4115](https://github.com/bridgecrewio/checkov/pull/4115)
- **terraform:** CKV2_AZURE_21 changed blob access type to private - [#3898](https://github.com/bridgecrewio/checkov/pull/3898)
- **terraform:** fix support for getting module-referenced resources context - [#4110](https://github.com/bridgecrewio/checkov/pull/4110)

### Platform

- **terraform:** add previous get_tf_definition_key function - [#4114](https://github.com/bridgecrewio/checkov/pull/4114)

## [2.2.180](https://github.com/bridgecrewio/checkov/compare/2.2.172...2.2.180) - 2022-12-19

### Feature

- **general:** Use --no-fail-on-crash to gracefully exit commit_repository and setup_bridgecrew_credentials - [#4099](https://github.com/bridgecrewio/checkov/pull/4099)
- **terraform_plan:** add check details to TF plan scan results - [#4091](https://github.com/bridgecrewio/checkov/pull/4091)
- **terraform:** new azurerm checks - App config - [#3988](https://github.com/bridgecrewio/checkov/pull/3988)
- **terraform:** Omit values from graph checks - [#4076](https://github.com/bridgecrewio/checkov/pull/4076)

### Bug Fix

- **general:** change env var name for no-fail-on-crash flag - [#4107](https://github.com/bridgecrewio/checkov/pull/4107)
- **github:** Fix GHA IR resource names in case of 2 identical images - [#4108](https://github.com/bridgecrewio/checkov/pull/4108)
- **terraform:** azurerm storage defaults - fix for storage case #3516 - [#4083](https://github.com/bridgecrewio/checkov/pull/4083)
- **terraform:** fix nested module resources ids in the report - [#4098](https://github.com/bridgecrewio/checkov/pull/4098)

## [2.2.172](https://github.com/bridgecrewio/checkov/compare/2.2.168...2.2.172) - 2022-12-18

### Feature

- **general:** Add no-fail-on-crash flag - [#4097](https://github.com/bridgecrewio/checkov/pull/4097)
- **gha:** add fix for gha graphs and UT - [#4084](https://github.com/bridgecrewio/checkov/pull/4084)
- **kubernetes:** inject k8s FF flags to instance instead of constructor - [#4096](https://github.com/bridgecrewio/checkov/pull/4096)

### Bug Fix

- **terraform:** add a method for get the entity definition path from the entity itself - [#4095](https://github.com/bridgecrewio/checkov/pull/4095)
- **terraform:** add address attribute to all scanned terraform blocks - [#4074](https://github.com/bridgecrewio/checkov/pull/4074)

## [2.2.168](https://github.com/bridgecrewio/checkov/compare/2.2.158...2.2.168) - 2022-12-15

### Feature

- **kubernetes:** Add kubernetes YAML checks to checkov packaging - [#4073](https://github.com/bridgecrewio/checkov/pull/4073)
- **kubernetes:** move whorf to dedicated repo - [#4062](https://github.com/bridgecrewio/checkov/pull/4062)
- **terraform_plan:** add Image Referencer for Terraform plan files - [#4063](https://github.com/bridgecrewio/checkov/pull/4063)
- **terraform:** add CKV NCP rules about AutoScalingGroup, Load Balancer - [#3821](https://github.com/bridgecrewio/checkov/pull/3821)
- **terraform:** add CKV NCP rules about Nat Gateways and Route - [#3854](https://github.com/bridgecrewio/checkov/pull/3854)
- **terraform:** combine tf plan and tf graphs for nested modules - [#4066](https://github.com/bridgecrewio/checkov/pull/4066)
- **terraform:** More azurerm checks for terraform - [#3970](https://github.com/bridgecrewio/checkov/pull/3970)

### Bug Fix

- **openapi:** Fix in PathSchemeDefineHTTP opeAPI check - [#4079](https://github.com/bridgecrewio/checkov/pull/4079)
- **terraform:** CKV_AZURE_43 add new test case - [#4082](https://github.com/bridgecrewio/checkov/pull/4082)

## [2.2.158](https://github.com/bridgecrewio/checkov/compare/2.2.155...2.2.158) - 2022-12-14

### Feature

- **github:** more CIS checks- part3  - [#4057](https://github.com/bridgecrewio/checkov/pull/4057)
- **terraform:** Adding yaml based build time policies for corresponding PC run time policies - [#3962](https://github.com/bridgecrewio/checkov/pull/3962)

### Bug Fix

- **secrets:** fix secrets crash when secret is non string - [#4077](https://github.com/bridgecrewio/checkov/pull/4077)

## [2.2.155](https://github.com/bridgecrewio/checkov/compare/2.2.148...2.2.155) - 2022-12-13

### Feature

- **github:**  more CIS checks- part2 - [#4017](https://github.com/bridgecrewio/checkov/pull/4017)
- **kubernetes:** added CKV2_K8S_EXAMPLE_1 only in tests as an example for k8s graph check for pod which is publicly accessible - [#4060](https://github.com/bridgecrewio/checkov/pull/4060)
- **kubernetes:** added deployment name to pod resource id - [#4040](https://github.com/bridgecrewio/checkov/pull/4040)
- **sca:** fix root packages fixed version - [#4070](https://github.com/bridgecrewio/checkov/pull/4070)

### Bug Fix

- **sca:** invoke packaging.Version instead of parse - [#4065](https://github.com/bridgecrewio/checkov/pull/4065)
- **secrets:** fix error when secret is None - [#4071](https://github.com/bridgecrewio/checkov/pull/4071)
- **terraform:** checkov fix as resource container_group modified - [#4061](https://github.com/bridgecrewio/checkov/pull/4061)
- **terraform:** fixed unexpected data for IAMPublicActionsPolicy - [#4067](https://github.com/bridgecrewio/checkov/pull/4067)
- **terraform:** fixed unexpected data for MonitorLogProfileRetentionDays - [#4068](https://github.com/bridgecrewio/checkov/pull/4068)

### Platform

- **general:** Apply licensing from platform - [#3961](https://github.com/bridgecrewio/checkov/pull/3961)

## [2.2.148](https://github.com/bridgecrewio/checkov/compare/2.2.139...2.2.148) - 2022-12-12

### Feature

- **gha:** Add gha graph infra - [#4058](https://github.com/bridgecrewio/checkov/pull/4058)
- **gha:** add infra for gha graphs - [#4052](https://github.com/bridgecrewio/checkov/pull/4052)
- **sca:**  fixed dependencies default value - [#4056](https://github.com/bridgecrewio/checkov/pull/4056)
- **sca:** added indirect cves fix versions - [#4023](https://github.com/bridgecrewio/checkov/pull/4023)
- **secrets:** Inject secrets omitter to runner registry - [#4054](https://github.com/bridgecrewio/checkov/pull/4054)
- **terraform_plan:** support jsonpath queries in AWS IAM policy strings for Terraform plan - [#4033](https://github.com/bridgecrewio/checkov/pull/4033)
- **terraform:** Extend secret attributes to omit mapping - [#4028](https://github.com/bridgecrewio/checkov/pull/4028)
- **terraform:** tf plan combine graphs pass params - [#4051](https://github.com/bridgecrewio/checkov/pull/4051)

### Bug Fix

- **terraform:** add missing resource aws_route53_resolver_endpoint #3968 - [#3995](https://github.com/bridgecrewio/checkov/pull/3995)
- **terraform:** fix getting local dest module path - [#4055](https://github.com/bridgecrewio/checkov/pull/4055)
- **terraform:** Fix some errors in Dynamic Blocks rendering - [#4050](https://github.com/bridgecrewio/checkov/pull/4050)

## [2.2.139](https://github.com/bridgecrewio/checkov/compare/2.2.130...2.2.139) - 2022-12-11

### Feature

- **graph:** Added `not_within` attribute solver for graph checks - [#4041](https://github.com/bridgecrewio/checkov/pull/4041)
- **kubernetes:** Add CKV2_K8S_2 graph check for potential privilege escalation in `nodes/proxy` or `pods/exec` with `create` permissions - [#4034](https://github.com/bridgecrewio/checkov/pull/4034)
- **kubernetes:** Add CKV2_K8S_3 no `impersonate` permissions for `ServiceAccount/Node` - [#4037](https://github.com/bridgecrewio/checkov/pull/4037)
- **kubernetes:** Added CKV2_K8S_4 check to not allow modifying of services/status - [#4038](https://github.com/bridgecrewio/checkov/pull/4038)
- **kubernetes:** Added CKV2_K8S_5 check that no service account or node can read all secrets - [#4042](https://github.com/bridgecrewio/checkov/pull/4042)
- **secrets:** Accepting json reports from bucket in secrets_omitter - [#4039](https://github.com/bridgecrewio/checkov/pull/4039)
- **terraform:** add CKV NCP rules about Route Table Association - [#3856](https://github.com/bridgecrewio/checkov/pull/3856)

### Bug Fix

- **kubernetes:** Corrected list format for yaml files in new k8s graph check tests - [#4035](https://github.com/bridgecrewio/checkov/pull/4035)
- **secrets:** custom secret add support for value str and not only list - [#4024](https://github.com/bridgecrewio/checkov/pull/4024)
- **terraform:** Fix in dot separator in the dynamic argument - [#4036](https://github.com/bridgecrewio/checkov/pull/4036)

## [2.2.130](https://github.com/bridgecrewio/checkov/compare/2.2.124...2.2.130) - 2022-12-08

### Feature

- **general:** Apply policy-level suppressions as skipped checks - [#4020](https://github.com/bridgecrewio/checkov/pull/4020)
- **github:** Add 3 CIS checks: 1.1.3, 1.1.8, 1.1.10 - [#4003](https://github.com/bridgecrewio/checkov/pull/4003)
- **kubernetes:** Added CKV2_K8S_1 to ensure RoleBinding do not allow privilege escalation to a ServiceAccount/Node - [#4004](https://github.com/bridgecrewio/checkov/pull/4004)
- **secrets:** Omit secrets from reports based on secrets reports - [#3991](https://github.com/bridgecrewio/checkov/pull/3991)
- **secrets:** Omit secrets from reports based on secrets reports - [#4015](https://github.com/bridgecrewio/checkov/pull/4015)

### Bug Fix

- **github:** remove secrets from schema example - [#4019](https://github.com/bridgecrewio/checkov/pull/4019)
- **terraform:** fix resource block address - [#4018](https://github.com/bridgecrewio/checkov/pull/4018)

## [2.2.124](https://github.com/bridgecrewio/checkov/compare/2.2.116...2.2.124) - 2022-12-07

### Feature

- **sca:** change sca packages output to include dependencies structure - [#3957](https://github.com/bridgecrewio/checkov/pull/3957)
- **secrets:** Adding check length for secret - [#3985](https://github.com/bridgecrewio/checkov/pull/3985)
- **terraform:** nested modules support in graph - [#3935](https://github.com/bridgecrewio/checkov/pull/3935)

### Bug Fix

- **circleci:** fix executors in resource_id - [#4008](https://github.com/bridgecrewio/checkov/pull/4008)
- **secrets:** Bump detect secrets version - [#3997](https://github.com/bridgecrewio/checkov/pull/3997)
- **terraform:** Fix an issue in dynamic blocks - [#4006](https://github.com/bridgecrewio/checkov/pull/4006)
- **terraform:** fix CKV_AWS_283 check - [#4005](https://github.com/bridgecrewio/checkov/pull/4005)
- **terraform:** Fix CKV_AZURE_168 check - [#4000](https://github.com/bridgecrewio/checkov/pull/4000)
- **terraform:** Fix some issues in dynamic blocks flow - [#4002](https://github.com/bridgecrewio/checkov/pull/4002)
- **terraform:** Fix TF checks crashes - [#3992](https://github.com/bridgecrewio/checkov/pull/3992)

## [2.2.116](https://github.com/bridgecrewio/checkov/compare/2.2.114...2.2.116) - 2022-12-06

### Feature

- **general:** Report failed attempts at reporting contributor metrics - [#3984](https://github.com/bridgecrewio/checkov/pull/3984)
- **kubernetes:** create simple resources id for pods; allow enabling k8s graph features using env vars - [#3975](https://github.com/bridgecrewio/checkov/pull/3975)
- **terraform:** check for insecure protocols - [#3958](https://github.com/bridgecrewio/checkov/pull/3958)
- **terraform:** Check resource-based policies for public access - [#3989](https://github.com/bridgecrewio/checkov/pull/3989)
- **terraform:** Dynamic Blocks support for loop in for_each attribute - [#3982](https://github.com/bridgecrewio/checkov/pull/3982)
- **terraform:** new aks checks for Azure - [#3951](https://github.com/bridgecrewio/checkov/pull/3951)

### Bug Fix

- **dockerfile:** fix Dockerfile inline skip handling - [#3976](https://github.com/bridgecrewio/checkov/pull/3976)
- **secrets:** fix_Record_code_block_secrets - [#3987](https://github.com/bridgecrewio/checkov/pull/3987)
- **terraform:** azurerm kusto cluster encryption - wrong attribute tested for - [#3972](https://github.com/bridgecrewio/checkov/pull/3972)

## [2.2.114](https://github.com/bridgecrewio/checkov/compare/2.2.112...2.2.114) - 2022-12-04

### Feature

- **terraform:** add CKV NCP rules about ncloud access control group rule - [#3860](https://github.com/bridgecrewio/checkov/pull/3860)

### Bug Fix

- **secrets:** fix Issue with 'NoneType' error in the custom detectors load_detectors - [#3973](https://github.com/bridgecrewio/checkov/pull/3973)

### Platform

- **terraform:** remove redundant exc_info for module without source - [#3974](https://github.com/bridgecrewio/checkov/pull/3974)

## [2.2.112](https://github.com/bridgecrewio/checkov/compare/2.2.106...2.2.112) - 2022-12-01

### Feature

- **dockerfile:** add graph to Dockerfile - [#3948](https://github.com/bridgecrewio/checkov/pull/3948)
- **terraform:** add CKV NCP rules about access control group Inbound rule. - [#3859](https://github.com/bridgecrewio/checkov/pull/3859)
- **terraform:** Implement relative file path standard for tf plan file runs - [#3918](https://github.com/bridgecrewio/checkov/pull/3918)

### Bug Fix

- **general:** fix doc links on windows - [#3959](https://github.com/bridgecrewio/checkov/pull/3959)
- **secrets:** Fix omitting of secrets that are json encoded - [#3964](https://github.com/bridgecrewio/checkov/pull/3964)
- **terraform_plan:** Fix k8s checks edgecases for terraform plan - [#3966](https://github.com/bridgecrewio/checkov/pull/3966)
- **terraform:** OCI Security Group Control Problem - [#3933](https://github.com/bridgecrewio/checkov/pull/3933)

### Platform

- **secrets:** remove the use of enable_secret_scan_all_files for custom secrets - [#3954](https://github.com/bridgecrewio/checkov/pull/3954)

### Documentation

- **terraform:** update Terraform modules docs - [#3965](https://github.com/bridgecrewio/checkov/pull/3965)

## [2.2.106](https://github.com/bridgecrewio/checkov/compare/2.2.105...2.2.106) - 2022-11-30

- no noteworthy changes

## [2.2.105](https://github.com/bridgecrewio/checkov/compare/2.2.99...2.2.105) - 2022-11-29

### Feature

- **terraform:** add CKV NCP rules about Load Balancer Listener Using HTTPS - [#3858](https://github.com/bridgecrewio/checkov/pull/3858)
- **terraform:** add CKV NCP rules about server instance and public IP - [#3857](https://github.com/bridgecrewio/checkov/pull/3857)
- **terraform:** azurerm ACR check for retention policy - [#3927](https://github.com/bridgecrewio/checkov/pull/3927)

## [2.2.99](https://github.com/bridgecrewio/checkov/compare/2.2.96...2.2.99) - 2022-11-27

### Feature

- **github:** add CIS checks part 1.  Most of the 1.1.x - [#3937](https://github.com/bridgecrewio/checkov/pull/3937)
- **terraform:** Azure ACR Enable Image Quarantine - [#3925](https://github.com/bridgecrewio/checkov/pull/3925)
- **terraform:** Azure use signed image in ACR - [#3923](https://github.com/bridgecrewio/checkov/pull/3923)

### Bug Fix

- **bicep:** ignore unresolvable properties for Bicep storage account checks - [#3946](https://github.com/bridgecrewio/checkov/pull/3946)
- **gha:** added test for step with no step name - [#3945](https://github.com/bridgecrewio/checkov/pull/3945)

## [2.2.96](https://github.com/bridgecrewio/checkov/compare/2.2.95...2.2.96) - 2022-11-26

- no noteworthy changes

## [2.2.95](https://github.com/bridgecrewio/checkov/compare/2.2.86...2.2.95) - 2022-11-24

### Feature

- **circleci:** add check for detecting images without check resource - [#3930](https://github.com/bridgecrewio/checkov/pull/3930)
- **terraform:** ACR container scanning - [#3922](https://github.com/bridgecrewio/checkov/pull/3922)
- **terraform:** add CKV NCP check about NKS(kubernetes) logging - [#3855](https://github.com/bridgecrewio/checkov/pull/3855)
- **terraform:** Adding yaml based build time policies for corresponding PC run time policies - [#3900](https://github.com/bridgecrewio/checkov/pull/3900)

### Bug Fix

- **general:** update checks_metadata structure - [#3929](https://github.com/bridgecrewio/checkov/pull/3929)
- **gha:** and circleci resource names  - [#3914](https://github.com/bridgecrewio/checkov/pull/3914)
- **kubernetes:** Handle invalid helm chart meta - [#3939](https://github.com/bridgecrewio/checkov/pull/3939)
- **sca:** fix related resource id for helm and kustomize - [#3931](https://github.com/bridgecrewio/checkov/pull/3931)
- **terraform:** better check names to avoid confusion - addresses #3912 - [#3921](https://github.com/bridgecrewio/checkov/pull/3921)
- **terraform:** CKV_AZURE_144 passes on defaults - [#3938](https://github.com/bridgecrewio/checkov/pull/3938)
- **terraform:** Removed duplicate check CKV_AZURE_60 - [#3928](https://github.com/bridgecrewio/checkov/pull/3928)

### Platform

- **secrets:** Support custom detectors from the platform - [#3926](https://github.com/bridgecrewio/checkov/pull/3926)

## [2.2.86](https://github.com/bridgecrewio/checkov/compare/2.2.84...2.2.86) - 2022-11-23

### Feature

- **terraform:** add CKV_AWS_282 to ensure that Redshift Serverless namespace is encrypted by KMS - [#3915](https://github.com/bridgecrewio/checkov/pull/3915)

### Bug Fix

- **terraform:** Remove cross variables edges duplications - [#3920](https://github.com/bridgecrewio/checkov/pull/3920)

## [2.2.84](https://github.com/bridgecrewio/checkov/compare/2.2.80...2.2.84) - 2022-11-22

### Feature

- **general:** sign and push checkov image to GitHub registry - [#3906](https://github.com/bridgecrewio/checkov/pull/3906)
- **secrets:** Add Terraform multiline secrets handling - [#3907](https://github.com/bridgecrewio/checkov/pull/3907)
- **terraform:** ensure snapshots use encryption - [#3899](https://github.com/bridgecrewio/checkov/pull/3899)
- **terraform:** support cross-modules edges - [#3909](https://github.com/bridgecrewio/checkov/pull/3909)

## [2.2.80](https://github.com/bridgecrewio/checkov/compare/2.2.78...2.2.80) - 2022-11-21

### Feature

- **terraform:** add nested module address attribute - [#3904](https://github.com/bridgecrewio/checkov/pull/3904)

## [2.2.78](https://github.com/bridgecrewio/checkov/compare/2.2.75...2.2.78) - 2022-11-20

### Feature

- **general:** add output format cyclonedx_json - [#3902](https://github.com/bridgecrewio/checkov/pull/3902)
- **general:** add source to contributor metrics report - [#3905](https://github.com/bridgecrewio/checkov/pull/3905)

### Bug Fix

- **terraform:** Fix an edge case in AbsRDSParameter check  - [#3903](https://github.com/bridgecrewio/checkov/pull/3903)

## [2.2.75](https://github.com/bridgecrewio/checkov/compare/2.2.72...2.2.75) - 2022-11-17

### Feature

- **github:** add output-file-path flag to checkov-action - [#3897](https://github.com/bridgecrewio/checkov/pull/3897)

### Bug Fix

- **terraform:** Dynamic blocks - added support for lookup null/true/false values - [#3893](https://github.com/bridgecrewio/checkov/pull/3893)

### Platform

- **sca:** added dependency tree format  - [#3892](https://github.com/bridgecrewio/checkov/pull/3892)

## [2.2.72](https://github.com/bridgecrewio/checkov/compare/2.2.65...2.2.72) - 2022-11-16

### Feature

- **terraform:** add CKV NCP rules about NKSPublicAccess - [#3822](https://github.com/bridgecrewio/checkov/pull/3822)
- **terraform:** Censor secrets from tfplan graph - [#3894](https://github.com/bridgecrewio/checkov/pull/3894)
- **terraform:** create cross-variable edges between resources from the same module - [#3881](https://github.com/bridgecrewio/checkov/pull/3881)

### Bug Fix

- **general:** remove filter value validation - [#3896](https://github.com/bridgecrewio/checkov/pull/3896)
- **terraform:** Fix dynamic blocks nested module - [#3890](https://github.com/bridgecrewio/checkov/pull/3890)
- **terraform:** handle empty enabled_cluster_log_types list - [#3891](https://github.com/bridgecrewio/checkov/pull/3891)

### Platform

- **sca:** add scaCliScanId parameter - [#3789](https://github.com/bridgecrewio/checkov/pull/3789)

## [2.2.65](https://github.com/bridgecrewio/checkov/compare/2.2.58...2.2.65) - 2022-11-15

### Feature

- **terraform:** test checks for any port access - [#3882](https://github.com/bridgecrewio/checkov/pull/3882)

### Bug Fix

- **terraform:** Fixing some broke flow in dynamic blocks rendering - [#3879](https://github.com/bridgecrewio/checkov/pull/3879)
- **terraform:** Not adding dynamic blocks attributes to attributes - [#3872](https://github.com/bridgecrewio/checkov/pull/3872)

### Platform

- **general:** Support s3 client config for govcloud - [#3880](https://github.com/bridgecrewio/checkov/pull/3880)
- **sca:** Add repoId to GET request - [#3876](https://github.com/bridgecrewio/checkov/pull/3876)
- **sca:** Fix bom report - [#3867](https://github.com/bridgecrewio/checkov/pull/3867)
- **sca:** Poll sca scan results using Polling API - [#3841](https://github.com/bridgecrewio/checkov/pull/3841)
- **sca:** remove src from repo path - [#3884](https://github.com/bridgecrewio/checkov/pull/3884)

## [2.2.58](https://github.com/bridgecrewio/checkov/compare/2.2.50...2.2.58) - 2022-11-14

### Feature

- **general:** number of words larger/less than or equal operators - [#3827](https://github.com/bridgecrewio/checkov/pull/3827)
- **general:** remove env var for running contributor metrics report and add logs - [#3873](https://github.com/bridgecrewio/checkov/pull/3873)
- **terraform:** add CKV NCP rules about Load Balancer Exposed to Internet - [#3819](https://github.com/bridgecrewio/checkov/pull/3819)
- **terraform:** Mask secret values in Terraform plan file reports by resource - [#3868](https://github.com/bridgecrewio/checkov/pull/3868)
- **terraform:** Support dynamic blocks with nested attributes - [#3869](https://github.com/bridgecrewio/checkov/pull/3869)

### Bug Fix

- **general:** Fixed operator name for number_of_words_derivaties - [#3875](https://github.com/bridgecrewio/checkov/pull/3875)
- **terraform:** Fix dynamic attributes override each other - [#3866](https://github.com/bridgecrewio/checkov/pull/3866)

## [2.2.50](https://github.com/bridgecrewio/checkov/compare/2.2.44...2.2.50) - 2022-11-13

### Feature

- **general:** add reporting contributor metrics - [#3823](https://github.com/bridgecrewio/checkov/pull/3823)
- **terraform:** add CKV NCP rules about access key hard coding - [#3820](https://github.com/bridgecrewio/checkov/pull/3820)
- **terraform:** NSGRulePortAccessRestricted - Remove the condition for dynamic blocks - [#3862](https://github.com/bridgecrewio/checkov/pull/3862)

### Bug Fix

- **kubernetes:** handle empty spec object in k8s templates - [#3865](https://github.com/bridgecrewio/checkov/pull/3865)
- **openapi:** fixed error in invalid openapi template - [#3863](https://github.com/bridgecrewio/checkov/pull/3863)
- **terraform:** app_service Upgrade tests and add web app resources - [#3838](https://github.com/bridgecrewio/checkov/pull/3838)
- **terraform:** Handled nested unrendered vars - [#3853](https://github.com/bridgecrewio/checkov/pull/3853)

## [2.2.44](https://github.com/bridgecrewio/checkov/compare/2.2.43...2.2.44) - 2022-11-11

### Bug Fix

- **terraform:** fix an issue with dynamics replacing a whole block - [#3846](https://github.com/bridgecrewio/checkov/pull/3846)

## [2.2.43](https://github.com/bridgecrewio/checkov/compare/2.2.38...2.2.43) - 2022-11-10

### Feature

- **terraform:** Wrap render dynamic blocks flow with try except - [#3837](https://github.com/bridgecrewio/checkov/pull/3837)

### Bug Fix

- **bicep:** make ARM AKS checks compatible with Bicep - [#3836](https://github.com/bridgecrewio/checkov/pull/3836)
- **cloudformation:** only parse valid tag key-pairs in CloudFormation - [#3835](https://github.com/bridgecrewio/checkov/pull/3835)
- **general:** Clear details before next check run to avoid duplications in output - [#3711](https://github.com/bridgecrewio/checkov/pull/3711)

## [2.2.38](https://github.com/bridgecrewio/checkov/compare/2.2.35...2.2.38) - 2022-11-09

### Feature

- **secrets:** add abstract multiline parser + implement multiline json parser - [#3799](https://github.com/bridgecrewio/checkov/pull/3799)
- **terraform:** Support for nested dynamic modules - [#3813](https://github.com/bridgecrewio/checkov/pull/3813)

### Bug Fix

- **kubernetes:** fixed unexpected list object - [#3833](https://github.com/bridgecrewio/checkov/pull/3833)

## [2.2.35](https://github.com/bridgecrewio/checkov/compare/2.2.31...2.2.35) - 2022-11-08

### Feature

- **general:** Added Number of Words operator - [#3801](https://github.com/bridgecrewio/checkov/pull/3801)
- **terraform:** add CKV NCP rules about LBTargetGroupUsingHTTPS - [#3797](https://github.com/bridgecrewio/checkov/pull/3797)
- **terraform:** add CKV NCP rules about NASEncrytionEnabled - [#3796](https://github.com/bridgecrewio/checkov/pull/3796)
- **terraform:** Add Env Var for rendering Dynamic Blocks - [#3816](https://github.com/bridgecrewio/checkov/pull/3816)
- **terraform:** Dynamic blocks breadcrumbs support - [#3814](https://github.com/bridgecrewio/checkov/pull/3814)
- **terraform:** PC Policy Team Yaml Policies Check-in - [#3785](https://github.com/bridgecrewio/checkov/pull/3785)
- **terraform:** PC-Policy-Team: Ensure GCP compute firewall ingress does not allow unrestricted access to all ports - [#3786](https://github.com/bridgecrewio/checkov/pull/3786)

### Platform

- **sca:** Run package scan using API - [#3812](https://github.com/bridgecrewio/checkov/pull/3812)

## [2.2.31](https://github.com/bridgecrewio/checkov/compare/2.2.22...2.2.31) - 2022-11-07

### Feature

- **azure:** Add get resource names for azure_pipelines - [#3798](https://github.com/bridgecrewio/checkov/pull/3798)
- **github:** add graph to GitHub Actions - [#3672](https://github.com/bridgecrewio/checkov/pull/3672)
- **terraform:** add CKV NCP rules about LBListenerUsesSecureProtocols - [#3782](https://github.com/bridgecrewio/checkov/pull/3782)
- **terraform:** Dynamic Modules Support map type - [#3800](https://github.com/bridgecrewio/checkov/pull/3800)
- **terraform:** include pods of kubernetes_deployment in kubernetes_pod checks (1/4) - [#3691](https://github.com/bridgecrewio/checkov/pull/3691)
- **terraform:** include pods of kubernetes_deployment in kubernetes_pod checks (2/4) - [#3702](https://github.com/bridgecrewio/checkov/pull/3702)
- **terraform:** include pods of kubernetes_deployment in kubernetes_pod checks (3/4) - [#3703](https://github.com/bridgecrewio/checkov/pull/3703)
- **terraform:** include pods of kubernetes_deployment in kubernetes_pod checks (4/4) - [#3738](https://github.com/bridgecrewio/checkov/pull/3738)

### Bug Fix

- **arm:** CKV_AZURE_9 & CKV_AZURE_10 - Scan fails if protocol value is a wildcard - [#3750](https://github.com/bridgecrewio/checkov/pull/3750)
- **azure:** Remove redundant file path from resource name in azure pipelines - [#3818](https://github.com/bridgecrewio/checkov/pull/3818)
- **secrets:** fix slow secrets scan in yaml files - [#3803](https://github.com/bridgecrewio/checkov/pull/3803)
- **secrets:** fixed path of secrets tests to exclude - [#3817](https://github.com/bridgecrewio/checkov/pull/3817)
- **terraform:** fix gke resource name not string - [#3811](https://github.com/bridgecrewio/checkov/pull/3811)

### Platform

- **general:** rationalize policy metadata error handling behavior - [#3795](https://github.com/bridgecrewio/checkov/pull/3795)
- **sca:** add new sca package scan - [#3802](https://github.com/bridgecrewio/checkov/pull/3802)
- **sca:** Extract checkov check links - [#3790](https://github.com/bridgecrewio/checkov/pull/3790)

## [2.2.22](https://github.com/bridgecrewio/checkov/compare/2.2.21...2.2.22) - 2022-11-06

### Feature

- **kubernetes:** Create keyword and network policy edge builders - [#3763](https://github.com/bridgecrewio/checkov/pull/3763)

## [2.2.21](https://github.com/bridgecrewio/checkov/compare/2.2.17...2.2.21) - 2022-11-03

### Feature

- **general:** add range_includes and inverted operator - [#3752](https://github.com/bridgecrewio/checkov/pull/3752)
- **secrets:** Add multiline detection to entropy keyword combinator - [#3788](https://github.com/bridgecrewio/checkov/pull/3788)

### Bug Fix

- **terraform:** render list entries via modules correctly - [#3781](https://github.com/bridgecrewio/checkov/pull/3781)

## [2.2.17](https://github.com/bridgecrewio/checkov/compare/2.2.15...2.2.17) - 2022-11-02

### Feature

- **terraform:** Add CKV_AWS_276 to ensure that API Gateway Method Settings data_trace_enabled is not set to True - [#3761](https://github.com/bridgecrewio/checkov/pull/3761)

### Bug Fix

- **terraform:** Fix `related_resource_id` for ImageReferencer in `external_module` - [#3780](https://github.com/bridgecrewio/checkov/pull/3780)

### Documentation

- **general:** Fix typo in docs - [#3694](https://github.com/bridgecrewio/checkov/pull/3694)

## [2.2.15](https://github.com/bridgecrewio/checkov/compare/2.2.8...2.2.15) - 2022-10-31

### Feature

- **github:** split repo and org webhooks to separate files - [#3764](https://github.com/bridgecrewio/checkov/pull/3764)
- **gitlab:** Adding image detection check to gitlab ci - [#3774](https://github.com/bridgecrewio/checkov/pull/3774)
- **openapi:** pre-validate OpenAPI JSON files - [#3760](https://github.com/bridgecrewio/checkov/pull/3760)

### Bug Fix

- **azure:** Support .yaml extension - [#3767](https://github.com/bridgecrewio/checkov/pull/3767)
- **github:** print the result again in GHA - [#3751](https://github.com/bridgecrewio/checkov/pull/3751)
- **terraform:** reduce parsing time for large TF plan files - [#3757](https://github.com/bridgecrewio/checkov/pull/3757)

## [2.2.8](https://github.com/bridgecrewio/checkov/compare/2.2.5...2.2.8) - 2022-10-30

### Feature

- **terraform:** add CKV2_AWS_40 to Ensure AWS IAM policy does not allow full IAM privileges - [#3712](https://github.com/bridgecrewio/checkov/pull/3712)

### Platform

- **general:** Get resources from platform and filter taggable resources for policies - [#3621](https://github.com/bridgecrewio/checkov/pull/3621)

## [2.2.5](https://github.com/bridgecrewio/checkov/compare/2.2.0...2.2.5) - 2022-10-27

### Feature

- **graph:** add support for modules in graph checks - [#3635](https://github.com/bridgecrewio/checkov/pull/3635)
- **terraform:** add CKV NCP rules about Network ACL. - [#3668](https://github.com/bridgecrewio/checkov/pull/3668)
- **terraform:** TF Dynamic Blocks support - `for_each` lists type - [#3737](https://github.com/bridgecrewio/checkov/pull/3737)

### Bug Fix

- **terraform:** fix a TF plan issue with CKV_AWS_274 - [#3747](https://github.com/bridgecrewio/checkov/pull/3747)
- **terraform:** fix false positive for write ACL yaml check - [#3745](https://github.com/bridgecrewio/checkov/pull/3745)

### Documentation

- **general:** Update Jenkins page to use Checkov image - [#3725](https://github.com/bridgecrewio/checkov/pull/3725)

## [2.2.0](https://github.com/bridgecrewio/checkov/compare/2.1.294...2.2.0) - 2022-10-26

### Breaking Change

- **github:** Change github_failed_only output suffix to .md - [#3595](https://github.com/bridgecrewio/checkov/pull/3595)
- **terraform:** adjust the check result return for dependant variables to unknown in  Python based checks - [#3743](https://github.com/bridgecrewio/checkov/pull/3743)
- **terraform:** return UNKNOWN for unrendered values in graph checks - [#3689](https://github.com/bridgecrewio/checkov/pull/3689)

### Feature

- **terraform:** add CKV NCP rule about block storage encryption. - [#3628](https://github.com/bridgecrewio/checkov/pull/3628)
- **terraform:** add CKV NCP rule about vpc volume encryption. - [#3629](https://github.com/bridgecrewio/checkov/pull/3629)
- **terraform:** add CKV NCP rules about Network ACL. - [#3630](https://github.com/bridgecrewio/checkov/pull/3630)
- **terraform:** Create checks for aws managed admin policy - [#3741](https://github.com/bridgecrewio/checkov/pull/3741)

### Bug Fix

- **terraform:** local_authentication_disabled - cosmodb check to look at SQL Api only CKV_AZURE_140 - [#3648](https://github.com/bridgecrewio/checkov/pull/3648)

## [2.1.294](https://github.com/bridgecrewio/checkov/compare/2.1.290...2.1.294) - 2022-10-25

### Feature

- **kubernetes:** Create label selector edge builder - [#3715](https://github.com/bridgecrewio/checkov/pull/3715)
- **terraform:** add CKV NCP rules about access control group Inbound rule. - [#3627](https://github.com/bridgecrewio/checkov/pull/3627)
- **terraform:** add versioned kubernetes resources to terraform kubernetes checks (5/5) - [#3657](https://github.com/bridgecrewio/checkov/pull/3657)

### Bug Fix

- **general:** skip scanning VCS configuration if only files are passed in - [#3729](https://github.com/bridgecrewio/checkov/pull/3729)

## [2.1.290](https://github.com/bridgecrewio/checkov/compare/2.1.288...2.1.290) - 2022-10-24

### Feature

- **circleci:** CircleCI Image Reference using Mixin class - [#3707](https://github.com/bridgecrewio/checkov/pull/3707)

### Bug Fix

- **kubernetes:** fix in CPURequests check - [#3727](https://github.com/bridgecrewio/checkov/pull/3727)

## [2.1.288](https://github.com/bridgecrewio/checkov/compare/2.1.286...2.1.288) - 2022-10-24

### Bug Fix

- **github:** fix GITHUB_OUTPUT and GITHUB_ENV issues of checkov-action - [#3726](https://github.com/bridgecrewio/checkov/pull/3726)
- **gitlab:** Modify gitlab ci resource id - [#3706](https://github.com/bridgecrewio/checkov/pull/3706)

## [2.1.286](https://github.com/bridgecrewio/checkov/compare/2.1.282...2.1.286) - 2022-10-23

### Feature

- **graph:** equals/not_equals_ignore_case operators (solvers) - [#3698](https://github.com/bridgecrewio/checkov/pull/3698)

### Bug Fix

- **github:** Fix GHA off value error resulting in checkov hanging - [#3713](https://github.com/bridgecrewio/checkov/pull/3713)
- **gitlab:** vcs gitlab groups retrieval - [#3716](https://github.com/bridgecrewio/checkov/pull/3716)
- **kubernetes:** fix in ServiceAccountTokens check - [#3717](https://github.com/bridgecrewio/checkov/pull/3717)
- **terraform:** Add debug logs to yaml parsing logic - [#3718](https://github.com/bridgecrewio/checkov/pull/3718)

## [2.1.282](https://github.com/bridgecrewio/checkov/compare/2.1.277...2.1.282) - 2022-10-20

### Bug Fix

- **general:** Custom Policies integration must run before Suppresion integration - [#3701](https://github.com/bridgecrewio/checkov/pull/3701)
- **terraform:** Add or condition for TLS 1.3 policy, supporting CKV_AWS_103 - [#3700](https://github.com/bridgecrewio/checkov/pull/3700)
- **terraform:** Fix TF AbsGoogleComputeFirewallUnrestrictedIngress check - [#3704](https://github.com/bridgecrewio/checkov/pull/3704)

## [2.1.277](https://github.com/bridgecrewio/checkov/compare/2.1.273...2.1.277) - 2022-10-19

### Feature

- **terraform:** add CKV NCP rules about access control group outbound rule. - [#3624](https://github.com/bridgecrewio/checkov/pull/3624)
- **terraform:** add versioned kubernetes resources to terraform kubernetes checks (2/5) - [#3654](https://github.com/bridgecrewio/checkov/pull/3654)
- **terraform:** add versioned kubernetes resources to terraform kubernetes checks (3/5) - [#3655](https://github.com/bridgecrewio/checkov/pull/3655)
- **terraform:** add versioned kubernetes resources to terraform kubernetes checks (4/5) - [#3656](https://github.com/bridgecrewio/checkov/pull/3656)

### Bug Fix

- **cloudformation:** Fix ALBListenerTLS12 check - [#3697](https://github.com/bridgecrewio/checkov/pull/3697)
- **helm:** undo file_abs_path manipulation for helm files - [#3692](https://github.com/bridgecrewio/checkov/pull/3692)
- **kubernetes:** Couple of fixes in Checks - [#3686](https://github.com/bridgecrewio/checkov/pull/3686)
- **terraform:** Fix CloudArmorWAFACLCVE202144228 check - [#3696](https://github.com/bridgecrewio/checkov/pull/3696)

## [2.1.273](https://github.com/bridgecrewio/checkov/compare/2.1.270...2.1.273) - 2022-10-18

### Feature

- **kustomize:** stop kustomize run, if there is nothing to process - [#3681](https://github.com/bridgecrewio/checkov/pull/3681)
- **sca:** Enable multiple image referencer framework results in the same scan - [#3652](https://github.com/bridgecrewio/checkov/pull/3652)
- **terraform:** add versioned kubernetes resources to terraform kubernetes checks (1/5) - [#3653](https://github.com/bridgecrewio/checkov/pull/3653)

### Documentation

- **general:** Fix broken links - [#3685](https://github.com/bridgecrewio/checkov/pull/3685)

## [2.1.270](https://github.com/bridgecrewio/checkov/compare/2.1.269...2.1.270) - 2022-10-13

### Bug Fix

- **terraform:** Outdated check for google_container_cluster binary authorization - [#3612](https://github.com/bridgecrewio/checkov/pull/3612)

## [2.1.269](https://github.com/bridgecrewio/checkov/compare/2.1.266...2.1.269) - 2022-10-12

### Feature

- **terraform:** Added new Terraform-AWS python IAMUserNotUsedForAccess(CKV_AWS_273) policy - [#3574](https://github.com/bridgecrewio/checkov/pull/3574)

### Bug Fix

- **argo:** only scan Argo Workflows files - [#3644](https://github.com/bridgecrewio/checkov/pull/3644)
- **kubernetes:** minor fix for getting entity type from template - [#3645](https://github.com/bridgecrewio/checkov/pull/3645)
- **kustomize:** add --client=true to kubectl version command, to prevent checkov waiting for timeout if cluster is unreachable - [#3641](https://github.com/bridgecrewio/checkov/pull/3641)
- **terraform:** update CKV_AWS_213 to also cover AWS predefined security policies - [#3615](https://github.com/bridgecrewio/checkov/pull/3615)

## [2.1.266](https://github.com/bridgecrewio/checkov/compare/2.1.258...2.1.266) - 2022-10-11

### Feature

- **general:** add Azure Pipelines framework - [#3579](https://github.com/bridgecrewio/checkov/pull/3579)

### Bug Fix

- **dockerfile:** handle quoted absolute path in CKV_DOCKER_10  - [#3626](https://github.com/bridgecrewio/checkov/pull/3626)
- **kubernetes:** handled missing field secretKeyRef in template - [#3639](https://github.com/bridgecrewio/checkov/pull/3639)
- **kubernetes:** handled missing key in k8s templates - [#3640](https://github.com/bridgecrewio/checkov/pull/3640)
- **terraform:** extend CKV2_AWS_15 to support aws_lb_target_group - [#3617](https://github.com/bridgecrewio/checkov/pull/3617)
- **terraform:** handle unexpected value for enabled_cloudwatch_logs_exports - [#3638](https://github.com/bridgecrewio/checkov/pull/3638)

## [2.1.258](https://github.com/bridgecrewio/checkov/compare/2.1.255...2.1.258) - 2022-10-06

### Feature

- **dockerfile:** add Image Referencer for Dockerfile - [#3571](https://github.com/bridgecrewio/checkov/pull/3571)

### Bug Fix

- **cloudformation:** Fixed unexpected null properties for LaunchConfigurationEBSEncryption - [#3620](https://github.com/bridgecrewio/checkov/pull/3620)

## [2.1.255](https://github.com/bridgecrewio/checkov/compare/2.1.254...2.1.255) - 2022-10-04

### Feature

- **general:** allow file destination mapping via output-file-path flag - [#3593](https://github.com/bridgecrewio/checkov/pull/3593)

## [2.1.254](https://github.com/bridgecrewio/checkov/compare/2.1.247...2.1.254) - 2022-10-03

### Feature

- **github:** GHA Image Referencer using IR Mixin class - [#3583](https://github.com/bridgecrewio/checkov/pull/3583)
- **graph:** add support for guideline field to custom graph checks - [#3600](https://github.com/bridgecrewio/checkov/pull/3600)
- **sca:** Add root path references to shorten file paths in Image Referencer results - [#3609](https://github.com/bridgecrewio/checkov/pull/3609)
- **sca:** support Image referencer in CLI - [#3601](https://github.com/bridgecrewio/checkov/pull/3601)

### Bug Fix

- **github:** bug fixes in CKV_GITHUB_6, CKV_GITHUB_7, CKV_GITHUB_9 - [#3605](https://github.com/bridgecrewio/checkov/pull/3605)
- **github:** Fix resource id and file path for GHA IR - [#3610](https://github.com/bridgecrewio/checkov/pull/3610)
- **terraform:** extend check for google cloud functions 2nd generation - [#3607](https://github.com/bridgecrewio/checkov/pull/3607)
- **terraform:** fix port is bool ingress rule - [#3606](https://github.com/bridgecrewio/checkov/pull/3606)

## [2.1.247](https://github.com/bridgecrewio/checkov/compare/2.1.242...2.1.247) - 2022-10-02

### Feature

- **general:** added cli argument for extra resources in report - [#3588](https://github.com/bridgecrewio/checkov/pull/3588)
- **serverless:** added extra resources for serverless and dockerfile - [#3576](https://github.com/bridgecrewio/checkov/pull/3576)
- **terraform:** add CKV_NCP_1 about lb target group health check, CKV_NCP_2 about access control group description - [#3569](https://github.com/bridgecrewio/checkov/pull/3569)

### Bug Fix

- **cloudformation:** fix lc ebs encryption - [#3598](https://github.com/bridgecrewio/checkov/pull/3598)
- **github:** changed the schema to accept no description for org - [#3589](https://github.com/bridgecrewio/checkov/pull/3589)
- **secrets:** Skip secrets from files encoded with special codecs - [#3597](https://github.com/bridgecrewio/checkov/pull/3597)

## [2.1.242](https://github.com/bridgecrewio/checkov/compare/2.1.236...2.1.242) - 2022-09-29

### Breaking Change

- **general:** switch from black-list to block-list  - [#3581](https://github.com/bridgecrewio/checkov/pull/3581)

### Feature

- **kubernetes:** added resources mappings for roles objects - [#3582](https://github.com/bridgecrewio/checkov/pull/3582)

### Bug Fix

- **github:** fix variables initialization - [#3585](https://github.com/bridgecrewio/checkov/pull/3585)
- **kubernetes:** Handle templates without name for PeerClientCertAuthTrue check - [#3577](https://github.com/bridgecrewio/checkov/pull/3577)
- **openapi:** fix openapi schema bug - [#3587](https://github.com/bridgecrewio/checkov/pull/3587)
- **sca:** fix CycloneDX output for Docker images - [#3586](https://github.com/bridgecrewio/checkov/pull/3586)
- **secrets:** change entropy limit in Combinator plugin - [#3575](https://github.com/bridgecrewio/checkov/pull/3575)
- **terraform:** fix external modules ids in graph report - [#3584](https://github.com/bridgecrewio/checkov/pull/3584)
- **terraform:** Handle malformed database_flags for GCP DB checks - [#3578](https://github.com/bridgecrewio/checkov/pull/3578)

## [2.1.236](https://github.com/bridgecrewio/checkov/compare/2.1.229...2.1.236) - 2022-09-28

### Feature

- **general:** Add enforcement rules to entrypoint.sh - [#3573](https://github.com/bridgecrewio/checkov/pull/3573)
- **openapi:** add CKV_OPENAPI_7 to ensure http is not used in path definition - [#3547](https://github.com/bridgecrewio/checkov/pull/3547)
- **sca:** add Image Referencer for Kubernetes, Helm and Kustomize - [#3505](https://github.com/bridgecrewio/checkov/pull/3505)
- **terraform:** add CKV_AWS_272 to validate Lambda function code-signing - [#3556](https://github.com/bridgecrewio/checkov/pull/3556)
- **terraform:** add new gcp postgresql checks - [#3532](https://github.com/bridgecrewio/checkov/pull/3532)
- **terraform:** allow resources without values in TF plan - [#3563](https://github.com/bridgecrewio/checkov/pull/3563)

## [2.1.229](https://github.com/bridgecrewio/checkov/compare/2.1.228...2.1.229) - 2022-09-27

### Bug Fix

- **kubernetes:** [CKV_K8S_68] Remove unnecessary condition check from ApiServerAnonymousAuth.py - [#3543](https://github.com/bridgecrewio/checkov/pull/3543)

## [2.1.228](https://github.com/bridgecrewio/checkov/compare/2.1.227...2.1.228) - 2022-09-26

### Bug Fix

- **general:** use current branch name instead of master for the checkov-action  - [#3568](https://github.com/bridgecrewio/checkov/pull/3568)

## [2.1.227](https://github.com/bridgecrewio/checkov/compare/2.1.226...2.1.227) - 2022-09-23

### Documentation

- **general:** Multi skip docs - [#3561](https://github.com/bridgecrewio/checkov/pull/3561)

## [2.1.226](https://github.com/bridgecrewio/checkov/compare/2.1.223...2.1.226) - 2022-09-22

### Feature

- **gitlab:** GitlabCI ImageReferencer - [#3544](https://github.com/bridgecrewio/checkov/pull/3544)

### Bug Fix

- **secrets:** Bump bc-detect-secrets - [#3555](https://github.com/bridgecrewio/checkov/pull/3555)
- **terraform:** fix check CKV2_AZURE_8 - [#3554](https://github.com/bridgecrewio/checkov/pull/3554)

### Documentation

- **general:** Fix TOC rendering issue on checkov.io - [#3551](https://github.com/bridgecrewio/checkov/pull/3551)

## [2.1.223](https://github.com/bridgecrewio/checkov/compare/2.1.219...2.1.223) - 2022-09-21

### Feature

- **general:** Improve ComplexSolver run time - [#3548](https://github.com/bridgecrewio/checkov/pull/3548)
- **kubernetes:** create complex k8s vertices - [#3549](https://github.com/bridgecrewio/checkov/pull/3549)

### Bug Fix

- **general:** only add `helpUri` to SARIF if it is non-empty - [#3542](https://github.com/bridgecrewio/checkov/pull/3542)
- **kubernetes:** [CKV_K8S_140] Update ApiServerTlsCertAndKey.py to check RHS values  - [#3506](https://github.com/bridgecrewio/checkov/pull/3506)
- **kubernetes:** [CKV_K8S_90] Remove unnecessary condition check from ApiServerProfiling.py - [#3541](https://github.com/bridgecrewio/checkov/pull/3541)

## [2.1.219](https://github.com/bridgecrewio/checkov/compare/2.1.214...2.1.219) - 2022-09-20

### Feature

- **cloudformation:** add CKV_AWS_197 for CFN - [#3536](https://github.com/bridgecrewio/checkov/pull/3536)
- **sca:** Split `PRESENT_CACHED_RESULTS` env var to 2 feature flag like vars - [#3518](https://github.com/bridgecrewio/checkov/pull/3518)

### Bug Fix

- **general:** handle fixes for cloned OOTB policies - [#3535](https://github.com/bridgecrewio/checkov/pull/3535)
- **helm:** fix helm signal abort handler - [#3539](https://github.com/bridgecrewio/checkov/pull/3539)
- **terraform:** APIGatewayAuthorization check missing authorization - [#3545](https://github.com/bridgecrewio/checkov/pull/3545)
- **terraform:** fix tfvars rendering - [#3533](https://github.com/bridgecrewio/checkov/pull/3533)

## [2.1.214](https://github.com/bridgecrewio/checkov/compare/2.1.212...2.1.214) - 2022-09-19

### Feature

- **general:** leverage SARIF helpUri for guideline and SCA link - [#3492](https://github.com/bridgecrewio/checkov/pull/3492)
- **github:** Improving GHA schema validation - [#3513](https://github.com/bridgecrewio/checkov/pull/3513)
- **kubernetes:** added base class K8SEdgeBuilder - [#3530](https://github.com/bridgecrewio/checkov/pull/3530)
- **terraform:** GCP Cloud functions should not be public - [#3477](https://github.com/bridgecrewio/checkov/pull/3477)

### Bug Fix

- **github:** add missing schema files to distribution package - [#3537](https://github.com/bridgecrewio/checkov/pull/3537)
- **sca:** changes on cve suppressions to match package and image scan - [#3502](https://github.com/bridgecrewio/checkov/pull/3502)
- **sca:** send exception log when exceeded retries - [#3534](https://github.com/bridgecrewio/checkov/pull/3534)
- **terraform:**  make test case insensitive for CKV_ALI_35,CKV_ALI_36,CKV_ALI_37 - [#3507](https://github.com/bridgecrewio/checkov/pull/3507)
- **terraform:** do not evaluate OCI policy statements - [#3411](https://github.com/bridgecrewio/checkov/pull/3411)

## [2.1.212](https://github.com/bridgecrewio/checkov/compare/2.1.210...2.1.212) - 2022-09-18

### Bug Fix

- **helm:** helm add timeout to dependencies command - [#3525](https://github.com/bridgecrewio/checkov/pull/3525)
- **helm:** Helm fix logs - [#3524](https://github.com/bridgecrewio/checkov/pull/3524)

## [2.1.210](https://github.com/bridgecrewio/checkov/compare/2.1.207...2.1.210) - 2022-09-15

### Feature

- **sca:** add Image Referencer for CloudFormation - [#3501](https://github.com/bridgecrewio/checkov/pull/3501)

### Bug Fix

- **helm:** add try catch to helm cmd run - [#3508](https://github.com/bridgecrewio/checkov/pull/3508)

### Platform

- **general:** upload run metadata to S3 - [#3461](https://github.com/bridgecrewio/checkov/pull/3461)

## [2.1.207](https://github.com/bridgecrewio/checkov/compare/2.1.205...2.1.207) - 2022-09-14

### Feature

- **general:** fix format of cli command reference table - [#3504](https://github.com/bridgecrewio/checkov/pull/3504)

### Bug Fix

- **sca:** skip old CVE suppressions (without 'accountIds') - [#3503](https://github.com/bridgecrewio/checkov/pull/3503)

## [2.1.205](https://github.com/bridgecrewio/checkov/compare/2.1.204...2.1.205) - 2022-09-13

### Feature

- **general:** add flag for summary position - [#3497](https://github.com/bridgecrewio/checkov/pull/3497)

## [2.1.204](https://github.com/bridgecrewio/checkov/compare/2.1.201...2.1.204) - 2022-09-12

### Feature

- **sca:** licenses suppressions by type - [#3491](https://github.com/bridgecrewio/checkov/pull/3491)

### Bug Fix

- **arm:** unexpected data type in ACRAnonymousPullDisabled - [#3496](https://github.com/bridgecrewio/checkov/pull/3496)
- **general:** remove duplicated reports - [#3495](https://github.com/bridgecrewio/checkov/pull/3495)

## [2.1.201](https://github.com/bridgecrewio/checkov/compare/2.1.196...2.1.201) - 2022-09-08

### Feature

- **general:** `intersects/not_intersects` operators (solvers) - [#3482](https://github.com/bridgecrewio/checkov/pull/3482)

### Bug Fix

- **gha:** Gracefully handle bad GHA job definitions - [#3489](https://github.com/bridgecrewio/checkov/pull/3489)
- **sca:** do not skip the scan if BC_LIC is used with --check - [#3488](https://github.com/bridgecrewio/checkov/pull/3488)

## [2.1.196](https://github.com/bridgecrewio/checkov/compare/2.1.193...2.1.196) - 2022-09-07

### Bug Fix

- **kubernetes:** Validate k8s spec type - [#3483](https://github.com/bridgecrewio/checkov/pull/3483)
- **terraform:** removed duplicate check CKV_ALI_34 - [#3467](https://github.com/bridgecrewio/checkov/pull/3467)

## [2.1.193](https://github.com/bridgecrewio/checkov/compare/2.1.188...2.1.193) - 2022-09-06

### Bug Fix

- **cloudformation:** fix bug in cfn parser - [#3473](https://github.com/bridgecrewio/checkov/pull/3473)

### Platform

- **sca:** Add images data to image_cached_results for ImageReferencer scan - [#3468](https://github.com/bridgecrewio/checkov/pull/3468)
- **secrets:** modify checkov secrets scanner to scan all files based on ff - [#3474](https://github.com/bridgecrewio/checkov/pull/3474)

## [2.1.188](https://github.com/bridgecrewio/checkov/compare/2.1.184...2.1.188) - 2022-09-05

## Feature

- **cloudformation:** json parser support triple quote string - [#3463](https://github.com/bridgecrewio/checkov/pull/3463)

## Bug Fix

- **terraform:** gcp postgresql default values - [#3457](https://github.com/bridgecrewio/checkov/pull/3457)

## [2.1.184](https://github.com/bridgecrewio/checkov/compare/2.1.182...2.1.184) - 2022-09-04

## Platform

- **general:** trim API urls - [#3460](https://github.com/bridgecrewio/checkov/pull/3460)

## Documentation

- **general:** adjust example for custom check with guideline - [#3459](https://github.com/bridgecrewio/checkov/pull/3459)

## [2.1.182](https://github.com/bridgecrewio/checkov/compare/2.1.179...2.1.182) - 2022-09-02

## Feature

- **sca:** Added fix details to junitxml - [#3456](https://github.com/bridgecrewio/checkov/pull/3456)
- **terraform:** Added 5 python (CKV_AWS_267-271) and 2 yaml (CKV2_AWS_38-39) policies. - [#3438](https://github.com/bridgecrewio/checkov/pull/3438)

## [2.1.179](https://github.com/bridgecrewio/checkov/compare/2.1.176...2.1.179) - 2022-09-01

## Bug Fix

- **graph:** cache jsonpath attributes parser results - [#3451](https://github.com/bridgecrewio/checkov/pull/3451)

## Platform

- **general:** revert dropping checks metadata for empty reports - [#3453](https://github.com/bridgecrewio/checkov/pull/3453)

===================================
Kubernetes Collection Release Notes
===================================

.. contents:: Topics


v2.2.0
======

Minor Changes
-------------

- add support for in-memory kubeconfig in addition to file for k8s modules. (https://github.com/ansible-collections/kubernetes.core/pull/212).
- helm - add support for history_max cli parameter (https://github.com/ansible-collections/kubernetes.core/pull/164).
- k8s - add support for label_selectors options (https://github.com/ansible-collections/kubernetes.core/issues/43).
- k8s - add support for waiting on statefulsets (https://github.com/ansible-collections/kubernetes.core/pull/195).
- k8s_log - Add since-seconds parameter to the k8s_log module (https://github.com/ansible-collections/kubernetes.core/pull/142).
- new lookup plugin to support kubernetes kustomize feature. (https://github.com/ansible-collections/kubernetes.core/issues/39).
- re-enable turbo mode for collection. The default is initially set to off (https://github.com/ansible-collections/kubernetes.core/pull/169).

Bugfixes
--------

- common - import k8sdynamicclient directly to workaround Ansible upstream bug (https://github.com/ansible-collections/kubernetes.core/issues/162).
- connection plugin - add arguments information into censored command (https://github.com/ansible-collections/kubernetes.core/pull/196).
- fix resource cache not being used (https://github.com/ansible-collections/kubernetes.core/pull/228).
- k8s - Fixes a bug where diff was always returned when using apply or modifying an existing object, even when diff=no was specified. The module no longer returns diff unless requested and will now honor diff=no (https://github.com/ansible-collections/kubernetes.core/pull/146).
- k8s_cp - fix k8s_cp uploading when target container's WORKDIR is not '/' (https://github.com/ansible-collections/kubernetes.core/issues/222).
- k8s_exec - add missing deprecation notice to return_code for k8s_exec (https://github.com/ansible-collections/kubernetes.core/pull/233).
- k8s_exec - fix k8s_exec returning rc attribute,  to follow ansible's common return values (https://github.com/ansible-collections/kubernetes.core/pull/230).
- lookup - recommend query instead of lookup (https://github.com/ansible-collections/kubernetes.core/issues/147).
- support the ``template`` param in all collections depending on kubernetes.core (https://github.com/ansible-collections/kubernetes.core/pull/154).

New Plugins
-----------

Lookup
~~~~~~

- kustomize - Build a set of kubernetes resources using a 'kustomization.yaml' file.

New Modules
-----------

- k8s_cp - Copy files and directories to and from pod.
- k8s_drain - Drain, Cordon, or Uncordon node in k8s cluster

v2.1.1
======

Bugfixes
--------

- check auth params for existence, not whether they are true (https://github.com/ansible-collections/kubernetes.core/pull/151).

v2.1.0
======

Minor Changes
-------------

- remove cloud.common as default dependency (https://github.com/ansible-collections/kubernetes.core/pull/148).
- temporarily disable turbo mode (https://github.com/ansible-collections/kubernetes.core/pull/149).

v2.0.2
======

Bugfixes
--------

- Fix apply for k8s module when an array attribute from definition contains empty dict (https://github.com/ansible-collections/kubernetes.core/issues/113).
- rename the apply function to fix broken imports in Ansible 2.9 (https://github.com/ansible-collections/kubernetes.core/pull/135).

v2.0.1
======

Bugfixes
--------

- inventory - add community.kubernetes to list of plugin choices in k8s inventory (https://github.com/ansible-collections/kubernetes.core/pull/128).

v2.0.0
======

Major Changes
-------------

- k8s - deprecate merge_type=json. The JSON patch functionality has never worked (https://github.com/ansible-collections/kubernetes.core/pull/99).
- k8s_json_patch - split JSON patch functionality out into a separate module (https://github.com/ansible-collections/kubernetes.core/pull/99).
- replaces the openshift client with the official kubernetes client (https://github.com/ansible-collections/kubernetes.core/issues/34).

Minor Changes
-------------

- Add cache_file when DynamicClient is created (https://github.com/ansible-collections/kubernetes.core/pull/46).
- Add configmap and secret hash functionality (https://github.com/ansible-collections/kubernetes.core/pull/48).
- Add logic for cache file name generation (https://github.com/ansible-collections/kubernetes.core/pull/46).
- Replicate apply method in the DynamicClient (https://github.com/ansible-collections/kubernetes.core/pull/45).
- add ``proxy_headers`` option for authentication on k8s_xxx modules (https://github.com/ansible-collections/kubernetes.core/pull/58).
- add support for using tags when running molecule test suite (https://github.com/ansible-collections/kubernetes.core/pull/62).
- added documentation for ``kubernetes.core`` collection (https://github.com/ansible-collections/kubernetes.core/pull/50).
- common - removed ``KubernetesAnsibleModule``, use ``K8sAnsibleMixin`` instead (https://github.com/ansible-collections/kubernetes.core/pull/70).
- helm - add example for complex values in ``helm`` module (https://github.com/ansible-collections/kubernetes.core/issues/109).
- k8s - Handle list of definition for option `template` (https://github.com/ansible-collections/kubernetes.core/pull/49).
- k8s - `continue_on_error` option added (whether to continue on creation/deletion errors) (https://github.com/ansible-collections/kubernetes.core/pull/49).
- k8s - support ``patched`` value for ``state`` option. patched state is an existing resource that has a given patch applied (https://github.com/ansible-collections/kubernetes.core/pull/90).
- k8s - wait for all pods to update when rolling out daemonset changes (https://github.com/ansible-collections/kubernetes.core/pull/102).
- k8s_scale - ability to scale multiple resource using ``label_selectors`` (https://github.com/ansible-collections/kubernetes.core/pull/114).
- k8s_scale - new parameter to determine whether to continue or not on error when scaling multiple resources (https://github.com/ansible-collections/kubernetes.core/pull/114).
- kubeconfig - update ``kubeconfig`` file location in the documentation (https://github.com/ansible-collections/kubernetes.core/issues/53).
- remove old change log fragment files.
- remove the deprecated ``KubernetesRawModule`` class (https://github.com/ansible-collections/community.kubernetes/issues/232).
- replicate base resource for lists functionality (https://github.com/ansible-collections/kubernetes.core/pull/89).

Breaking Changes / Porting Guide
--------------------------------

- Drop python 2 support (https://github.com/ansible-collections/kubernetes.core/pull/86).
- helm_plugin - remove unused ``release_namespace`` parameter (https://github.com/ansible-collections/kubernetes.core/pull/85).
- helm_plugin_info - remove unused ``release_namespace`` parameter (https://github.com/ansible-collections/kubernetes.core/pull/85).
- k8s_cluster_info - returned apis as list to avoid being overwritten in case of multiple version (https://github.com/ansible-collections/kubernetes.core/pull/41).
- k8s_facts - remove the deprecated alias from k8s_facts to k8s_info (https://github.com/ansible-collections/kubernetes.core/pull/125).

Bugfixes
--------

- enable unit tests in CI (https://github.com/ansible-collections/community.kubernetes/pull/407).
- helm - Accept ``validate_certs`` with a ``context`` (https://github.com/ansible-collections/kubernetes.core/pull/74).
- helm - fix helm ignoring the kubeconfig context when passed through the ``context`` param or the ``K8S_AUTH_CONTEXT`` environment variable (https://github.com/ansible-collections/community.kubernetes/issues/385).
- helm - handle multiline output of ``helm plugin list`` command (https://github.com/ansible-collections/community.kubernetes/issues/399).
- k8s - fix merge_type option when set to json (https://github.com/ansible-collections/kubernetes.core/issues/54).
- k8s - lookup should return list even if single item is found (https://github.com/ansible-collections/kubernetes.core/issues/9).
- k8s inventory - remove extra trailing slashes from the hostname (https://github.com/ansible-collections/kubernetes.core/issues/52).

New Modules
-----------

- k8s_json_patch - Apply JSON patch operations to existing objects

v1.2.0
======

Minor Changes
-------------

- Adjust the documentation to clarify the fact ``wait_condition.status`` is a string.
- Adjust the name of parameters of ``helm`` and ``helm_info`` to match the documentation. No playbook change required.
- The Helm modules (``helm``, ``helm_info``, ``helm_plugin``, ``helm_plugin_info``, ``helm_plugin_repository``) accept the K8S environment variables like the other modules of the collections.
- helm - add a ``skip_crds`` option to skip the installation of CRDs when installing or upgrading a chart (https://github.com/ansible-collections/community.kubernetes/issues/296).
- helm - add optional support for helm diff (https://github.com/ansible-collections/community.kubernetes/issues/248).
- helm_template - add helm_template module to support template functionality (https://github.com/ansible-collections/community.kubernetes/issues/367).
- k8s - add a ``delete_options`` parameter to control garbage collection behavior when deleting a resource (https://github.com/ansible-collections/community.kubernetes/issues/253).
- k8s - add an example for downloading manifest file and applying (https://github.com/ansible-collections/community.kubernetes/issues/352).
- k8s - check if kubeconfig file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s - check if src file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s_exec - add a note about required permissions for the module (https://github.com/ansible-collections/community.kubernetes/issues/339).
- k8s_info - add information about api_version while returning facts (https://github.com/ansible-collections/community.kubernetes/pull/308).
- runtime.yml - update minimum Ansible version required for Kubernetes collection (https://github.com/ansible-collections/community.kubernetes/issues/314).

Bugfixes
--------

- helm - ``release_values`` makes ansible always show changed state (https://github.com/ansible-collections/community.kubernetes/issues/274)
- helm - make helm-diff plugin detection more reliable by splitting by any whitespace instead of explicit whitespace (``\s``) (https://github.com/ansible-collections/community.kubernetes/pull/362).
- helm - return values in check mode when release is not present (https://github.com/ansible-collections/community.kubernetes/issues/280).
- helm_plugin - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- helm_plugin_info - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- k8s - fix check_mode always showing changes when using stringData on Secrets (https://github.com/ansible-collections/community.kubernetes/issues/282).
- k8s - handle ValueError when namespace is not provided (https://github.com/ansible-collections/community.kubernetes/pull/330).
- respect the ``wait_timeout`` parameter in the ``k8s`` and ``k8s_info`` modules when a resource does not exist (https://github.com/ansible-collections/community.kubernetes/issues/344).

v1.1.1
======

Bugfixes
--------

- k8s - Fix sanity test 'compile' failing because of positional args (https://github.com/ansible-collections/community.kubernetes/issues/260).

v1.1.0
======

Major Changes
-------------

- k8s - Add support for template parameter (https://github.com/ansible-collections/community.kubernetes/pull/230).
- k8s_* - Add support for vaulted kubeconfig and src (https://github.com/ansible-collections/community.kubernetes/pull/193).

Minor Changes
-------------

- Add Makefile and downstream build script for kubernetes.core (https://github.com/ansible-collections/community.kubernetes/pull/197).
- Add execution environment metadata (https://github.com/ansible-collections/community.kubernetes/pull/211).
- Add probot stale bot configuration to autoclose issues (https://github.com/ansible-collections/community.kubernetes/pull/196).
- Added a contribution guide (https://github.com/ansible-collections/community.kubernetes/pull/192).
- Refactor module_utils (https://github.com/ansible-collections/community.kubernetes/pull/223).
- Replace KubernetesAnsibleModule class with dummy class (https://github.com/ansible-collections/community.kubernetes/pull/227).
- Replace KubernetesRawModule class with K8sAnsibleMixin (https://github.com/ansible-collections/community.kubernetes/pull/231).
- common - Do not mark task as changed when diff is irrelevant (https://github.com/ansible-collections/community.kubernetes/pull/228).
- helm - Add appVersion idempotence check to Helm (https://github.com/ansible-collections/community.kubernetes/pull/246).
- helm - Return status in check mode (https://github.com/ansible-collections/community.kubernetes/pull/192).
- helm - Support for single or multiple values files (https://github.com/ansible-collections/community.kubernetes/pull/93).
- helm_* - Support vaulted kubeconfig (https://github.com/ansible-collections/community.kubernetes/pull/229).
- k8s - SelfSubjectAccessReviews supported when 405 response received (https://github.com/ansible-collections/community.kubernetes/pull/237).
- k8s - add testcase for adding multiple resources using template parameter (https://github.com/ansible-collections/community.kubernetes/issues/243).
- k8s_info - Add support for wait (https://github.com/ansible-collections/community.kubernetes/pull/235).
- k8s_info - update custom resource example (https://github.com/ansible-collections/community.kubernetes/issues/202).
- kubectl plugin - correct console log (https://github.com/ansible-collections/community.kubernetes/issues/200).
- raw - Handle exception raised by underlying APIs (https://github.com/ansible-collections/community.kubernetes/pull/180).

Bugfixes
--------

- common - handle exception raised due to DynamicClient (https://github.com/ansible-collections/community.kubernetes/pull/224).
- helm - add replace parameter (https://github.com/ansible-collections/community.kubernetes/issues/106).
- k8s (inventory) - Set the connection plugin and transport separately (https://github.com/ansible-collections/community.kubernetes/pull/208).
- k8s (inventory) - Specify FQCN for k8s inventory plugin to fix use with Ansible 2.9 (https://github.com/ansible-collections/community.kubernetes/pull/250).
- k8s_info - add wait functionality (https://github.com/ansible-collections/community.kubernetes/issues/18).

v1.0.0
======

Major Changes
-------------

- helm_plugin - new module to manage Helm plugins (https://github.com/ansible-collections/community.kubernetes/pull/154).
- helm_plugin_info - new modules to gather information about Helm plugins (https://github.com/ansible-collections/community.kubernetes/pull/154).
- k8s_exec - Return rc for the command executed (https://github.com/ansible-collections/community.kubernetes/pull/158).

Minor Changes
-------------

- Ensure check mode results are as expected (https://github.com/ansible-collections/community.kubernetes/pull/155).
- Update base branch to 'main' (https://github.com/ansible-collections/community.kubernetes/issues/148).
- helm - Add support for K8S_AUTH_CONTEXT, K8S_AUTH_KUBECONFIG env (https://github.com/ansible-collections/community.kubernetes/pull/141).
- helm - Allow creating namespaces with Helm (https://github.com/ansible-collections/community.kubernetes/pull/157).
- helm - add aliases context for kube_context (https://github.com/ansible-collections/community.kubernetes/pull/152).
- helm - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/community.kubernetes/issues/140).
- helm_info - add aliases context for kube_context (https://github.com/ansible-collections/community.kubernetes/pull/152).
- helm_info - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/community.kubernetes/issues/140).
- k8s_exec - return RC for the command executed (https://github.com/ansible-collections/community.kubernetes/issues/122).
- k8s_info - Update example using vars (https://github.com/ansible-collections/community.kubernetes/pull/156).

Security Fixes
--------------

- kubectl - connection plugin now redact kubectl_token and kubectl_password in console log (https://github.com/ansible-collections/community.kubernetes/issues/65).
- kubectl - redacted token and password from console log (https://github.com/ansible-collections/community.kubernetes/pull/159).

Bugfixes
--------

- Test against stable ansible branch so molecule tests work (https://github.com/ansible-collections/community.kubernetes/pull/168).
- Update openshift requirements in k8s module doc (https://github.com/ansible-collections/community.kubernetes/pull/153).

New Modules
-----------

- helm_plugin - Manage Helm plugins
- helm_plugin_info - Gather information about Helm plugins

v0.11.1
=======

Major Changes
-------------

- Add changelog and fragments and document changelog process (https://github.com/ansible-collections/community.kubernetes/pull/131).

Minor Changes
-------------

- Add action groups for playbooks with module_defaults (https://github.com/ansible-collections/community.kubernetes/pull/107).
- Add requires_ansible version constraints to runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/126).
- Add sanity test ignore file for Ansible 2.11 (https://github.com/ansible-collections/community.kubernetes/pull/130).
- Add test for openshift apply bug (https://github.com/ansible-collections/community.kubernetes/pull/94).
- Add version_added to each new collection module (https://github.com/ansible-collections/community.kubernetes/pull/98).
- Check Python code using flake8 (https://github.com/ansible-collections/community.kubernetes/pull/123).
- Don't require project coverage check on PRs (https://github.com/ansible-collections/community.kubernetes/pull/102).
- Improve k8s Deployment and Daemonset wait conditions (https://github.com/ansible-collections/community.kubernetes/pull/35).
- Minor documentation fixes and use of FQCN in some examples (https://github.com/ansible-collections/community.kubernetes/pull/114).
- Remove action_groups_redirection entry from meta/runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/127).
- Remove deprecated ANSIBLE_METADATA field (https://github.com/ansible-collections/community.kubernetes/pull/95).
- Use FQCN in module docs and plugin examples (https://github.com/ansible-collections/community.kubernetes/pull/146).
- Use improved kubernetes diffs where possible (https://github.com/ansible-collections/community.kubernetes/pull/105).
- helm - add 'atomic' option (https://github.com/ansible-collections/community.kubernetes/pull/115).
- helm - minor code refactoring (https://github.com/ansible-collections/community.kubernetes/pull/110).
- helm_info and helm_repository - minor code refactor (https://github.com/ansible-collections/community.kubernetes/pull/117).
- k8s - Handle set object retrieved from lookup plugin (https://github.com/ansible-collections/community.kubernetes/pull/118).

Bugfixes
--------

- Fix suboption docs structure for inventory plugins (https://github.com/ansible-collections/community.kubernetes/pull/103).
- Handle invalid kubeconfig parsing error (https://github.com/ansible-collections/community.kubernetes/pull/119).
- Make sure Service changes run correctly in check_mode (https://github.com/ansible-collections/community.kubernetes/pull/84).
- k8s_info - remove unneccessary k8s_facts deprecation notice (https://github.com/ansible-collections/community.kubernetes/pull/97).
- k8s_scale - Fix scale wait and add tests (https://github.com/ansible-collections/community.kubernetes/pull/100).
- raw - handle condition when definition is none (https://github.com/ansible-collections/community.kubernetes/pull/139).

v0.11.0
=======

Major Changes
-------------

- helm - New module for managing Helm charts (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_info - New module for retrieving Helm chart information (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_repository - New module for managing Helm repositories (https://github.com/ansible-collections/community.kubernetes/pull/61).

Minor Changes
-------------

- Rename repository to ``community.kubernetes`` (https://github.com/ansible-collections/community.kubernetes/pull/81).

Bugfixes
--------

- Make sure extra files are not included in built collection (https://github.com/ansible-collections/community.kubernetes/pull/85).
- Update GitHub Actions workflow for better CI stability (https://github.com/ansible-collections/community.kubernetes/pull/78).
- k8s_log - Module no longer attempts to parse log as JSON (https://github.com/ansible-collections/community.kubernetes/pull/69).

New Modules
-----------

- helm - Manages Kubernetes packages with the Helm package manager
- helm_info - Get information from Helm package deployed inside the cluster
- helm_repository - Add and remove Helm repository

v0.10.0
=======

Major Changes
-------------

- k8s_exec - New module for executing commands on pods via Kubernetes API (https://github.com/ansible-collections/community.kubernetes/pull/14).
- k8s_log - New module for retrieving pod logs (https://github.com/ansible-collections/community.kubernetes/pull/16).

Minor Changes
-------------

- k8s - Added ``persist_config`` option for persisting refreshed tokens (https://github.com/ansible-collections/community.kubernetes/issues/49).

Security Fixes
--------------

- kubectl - Warn about information disclosure when using options like ``kubectl_password``, ``kubectl_extra_args``, and ``kubectl_token`` to pass data through to the command line using the ``kubectl`` connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/51).

Bugfixes
--------

- k8s - Add exception handling when retrieving k8s client (https://github.com/ansible-collections/community.kubernetes/pull/54).
- k8s - Fix argspec for 'elements' (https://github.com/ansible-collections/community.kubernetes/issues/13).
- k8s - Use ``from_yaml`` filter with lookup examples in ``k8s`` module documentation examples (https://github.com/ansible-collections/community.kubernetes/pull/56).
- k8s_service - Fix argspec (https://github.com/ansible-collections/community.kubernetes/issues/33).
- kubectl - Fix documentation in kubectl connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/52).

New Modules
-----------

- k8s_exec - Execute command in Pod
- k8s_log - Fetch logs from Kubernetes resources

v0.9.0
======

Major Changes
-------------

- k8s - Inventory source migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Lookup plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_auth - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_config_resource_name - Filter plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s_info - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_scale - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_service - Module migrated from Ansible 2.9 to Kubernetes collection.
- kubectl - Connection plugin migrated from Ansible 2.9 to Kubernetes collection.
- openshift - Inventory source migrated from Ansible 2.9 to Kubernetes collection.

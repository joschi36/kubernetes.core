#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.openshift_common import OpenShiftAnsibleModule, OpenShiftAnsibleException

DOCUMENTATION = '''
module: openshift_v1_cluster_network
short_description: OpenShift ClusterNetwork
description:
- Manage the lifecycle of a cluster_network object. Supports check mode, and attempts
  to to be idempotent.
version_added: 2.3.0
author: OpenShift (@openshift)
options:
  annotations:
    description:
    - Annotations is an unstructured key value map stored with a resource that may
      be set by external tools to store and retrieve arbitrary metadata. They are
      not queryable and should be preserved when modifying objects.
    type: dict
  api_key:
    description:
    - Token used to connect to the API.
  cert_file:
    description:
    - Path to a certificate used to authenticate with the API.
    type: path
  cluster_networks:
    description:
    - ClusterNetworks is a list of ClusterNetwork objects that defines the global
      overlay network's L3 space by specifying a set of CIDR and netmasks that the
      SDN can allocate addressed from.
    type: list
  context:
    description:
    - The name of a context found in the Kubernetes config file.
  debug:
    description:
    - Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log
    default: false
    type: bool
  force:
    description:
    - If set to C(True), and I(state) is C(present), an existing object will updated,
      and lists will be replaced, rather than merged.
    default: false
    type: bool
  host:
    description:
    - Provide a URL for acessing the Kubernetes API.
  hostsubnetlength:
    description:
    - HostSubnetLength is the number of bits of network to allocate to each node.
      eg, 8 would mean that each node would have a /24 slice of the overlay network
      for its pods
    type: int
  key_file:
    description:
    - Path to a key file used to authenticate with the API.
    type: path
  kubeconfig:
    description:
    - Path to an existing Kubernetes config file. If not provided, and no other connection
      options are provided, the openshift client will attempt to load the default
      configuration file from I(~/.kube/config.json).
    type: path
  labels:
    description:
    - Map of string keys and values that can be used to organize and categorize (scope
      and select) objects. May match selectors of replication controllers and services.
    type: dict
  name:
    description:
    - Name must be unique within a namespace. Is required when creating resources,
      although some resources may allow a client to request the generation of an appropriate
      name automatically. Name is primarily intended for creation idempotence and
      configuration definition. Cannot be updated.
  namespace:
    description:
    - Namespace defines the space within each name must be unique. An empty namespace
      is equivalent to the "default" namespace, but "default" is the canonical representation.
      Not all objects are required to be scoped to a namespace - the value of this
      field for those objects will be empty. Must be a DNS_LABEL. Cannot be updated.
  network:
    description:
    - Network is a CIDR string specifying the global overlay network's L3 space
  password:
    description:
    - Provide a password for connecting to the API. Use in conjunction with I(username).
  plugin_name:
    description:
    - PluginName is the name of the network plugin being used
  resource_definition:
    description:
    - Provide the YAML definition for the object, bypassing any modules parameters
      intended to define object attributes.
    type: dict
  service_network:
    description:
    - ServiceNetwork is the CIDR range that Service IP addresses are allocated from
  src:
    description:
    - Provide a path to a file containing the YAML definition of the object. Mutually
      exclusive with I(resource_definition).
    type: path
  ssl_ca_cert:
    description:
    - Path to a CA certificate used to authenticate with the API.
    type: path
  state:
    description:
    - Determines if an object should be created, patched, or deleted. When set to
      C(present), the object will be created, if it does not exist, or patched, if
      parameter values differ from the existing object's attributes, and deleted,
      if set to C(absent). A patch operation results in merging lists and updating
      dictionaries, with lists being merged into a unique set of values. If a list
      contains a dictionary with a I(name) or I(type) attribute, a strategic merge
      is performed, where individual elements with a matching I(name_) or I(type)
      are merged. To force the replacement of lists, set the I(force) option to C(True).
    default: present
    choices:
    - present
    - absent
  username:
    description:
    - Provide a username for connecting to the API.
  verify_ssl:
    description:
    - Whether or not to verify the API server's SSL certificates.
    type: bool
requirements:
- openshift == 0.4.0
'''

EXAMPLES = '''
'''

RETURN = '''
api_version:
  description: Requested API version
  type: string
cluster_network:
  type: complex
  returned: when I(state) = C(present)
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    cluster_networks:
      description:
      - ClusterNetworks is a list of ClusterNetwork objects that defines the global
        overlay network's L3 space by specifying a set of CIDR and netmasks that the
        SDN can allocate addressed from.
      type: list
      contains:
        cidr:
          description:
          - CIDR defines the total range of a cluster networks address space.
          type: str
        host_subnet_length:
          description:
          - HostSubnetLength is the number of bits of the accompanying CIDR address
            to allocate to each node. eg, 8 would mean that each node would have a
            /24 slice of the overlay network for its pods.
          type: int
    hostsubnetlength:
      description:
      - HostSubnetLength is the number of bits of network to allocate to each node.
        eg, 8 would mean that each node would have a /24 slice of the overlay network
        for its pods
      type: int
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    metadata:
      description:
      - Standard object's metadata.
      type: complex
    network:
      description:
      - Network is a CIDR string specifying the global overlay network's L3 space
      type: str
    plugin_name:
      description:
      - PluginName is the name of the network plugin being used
      type: str
    service_network:
      description:
      - ServiceNetwork is the CIDR range that Service IP addresses are allocated from
      type: str
'''


def main():
    try:
        module = OpenShiftAnsibleModule('cluster_network', 'v1')
    except OpenShiftAnsibleException as exc:
        # The helper failed to init, so there is no module object. All we can do is raise the error.
        raise Exception(exc.message)

    try:
        module.execute_module()
    except OpenShiftAnsibleException as exc:
        module.fail_json(msg="Module failed!", error=str(exc))


if __name__ == '__main__':
    main()

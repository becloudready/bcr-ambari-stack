#!/usr/bin/env python

"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management import *
import os

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

java64_home = config['hostLevelParams']['java_home']

hostname = config['hostname']

nifi_user = config['configurations']['sa-nifi-env']['nifi_user']
nifi_group = config['configurations']['sa-nifi-env']['nifi_group']
nifi_base_dir = config['configurations']['sa-nifi-env']['nifi_base_dir']
nifi_log_dir = config['configurations']['sa-nifi-env']['nifi_log_dir']
nifi_install_log = nifi_base_dir + '/nifi-install.log'
nifi_initial_mem = config['configurations']['sa-nifi-env']['nifi_initial_mem']
nifi_initial_max = config['configurations']['sa-nifi-env']['nifi_initial_max']
nifi_pid_dir = config['configurations']['sa-nifi-env']['nifi_pid_dir']
nifi_pid_file = format("{nifi_pid_dir}/nifi.pid")
nifi_install_tmp_dir = nifi_base_dir + '/tmp'

http_proxy=config['configurations']['sa-nifi-env']['http_proxy']
https_proxy=config['configurations']['sa-nifi-env']['https_proxy']

zookeeper_servers = config['configurations']['sa-nifi-config']['zookeeper_quorum']
zk_port = config['configurations']['sa-nifi-config']['zk_port']
nifi_download = config['configurations']['sa-nifi-config']['nifi_download']


## Load Nifi Properties variables

nifi_flow_archive_max_time = config['configurations']['sa-nifi-properties']['nifi.flow.configuration.archive.max.time']
nifi_flow_archive_max_storage = config['configurations']['sa-nifi-properties']['nifi.flow.configuration.archive.max.storage']
nifi_flow_configuration_archive_max_count = config['configurations']['sa-nifi-properties']['nifi.flow.configuration.archive.max.count']
nifi_web_http_network_interface_default = config['configurations']['sa-nifi-properties']['nifi.web.http.network.interface.default']
nifi_web_https_network_interface_default = config['configurations']['sa-nifi-properties']['nifi.web.https.network.interface.default']
nifi_provenance_repository_debug_frequency = config['configurations']['sa-nifi-properties']['nifi.provenance.repository.debug.frequency']
nifi_provenance_repository_encryption_key_provider_implementation = config['configurations']['sa-nifi-properties']['nifi.provenance.repository.encryption.key.provider.implementation']
nifi_provenance_repository_encryption_key_provider_location = config['configurations']['sa-nifi-properties']['nifi.provenance.repository.encryption.key.provider.location']
nifi_provenance_repository_encryption_key_id = config['configurations']['sa-nifi-properties']['nifi.provenance.repository.encryption.key.id']
nifi_provenance_repository_encryption_key = config['configurations']['sa-nifi-properties']['nifi.provenance.repository.encryption.key']
nifi_cluster_node_protocol_max_threads = config['configurations']['sa-nifi-properties']['nifi.cluster.node.protocol.max.threads']


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

import sys
import os
import glob
import pwd
import grp
import signal
import time
from resource_management import *


class Master(Script):

    def install(self, env):
        import params
        env.set_params(params)
        Execute(format("rm -rf {params.nifi_base_dir}"))
        if params.https_proxy == 'no_proxy' or params.http_proxy == 'no_proxy':
            Execute(format("wget -qO- {params.nifi_download} | tar xvz -C /opt --transform 's/nifi-1.4.0/nifi/'"))
        else:   
            Execute(format("export https_proxy={params.https_proxy};  wget -qO- {params.nifi_download} | tar xvz -C /opt --transform 's/nifi-1.4.0/nifi/'"))

     

    def configure(self, env):
        # Import properties defined in -config.xml file from the params class
        import params 
        env.set_params(params)

        for config_files in [ 'sa-nifi-authorizers-env', 'sa-nifi-bootstrap-notification-services-env' ,
        'sa-nifi-jaas-conf', 'sa-nifi-login-identity-providers-env', 'sa-nifi-logsearch-conf', 'sa-nifi-node-logback-env',
         'sa-nifi-state-management-env']:
        
            configurations = params.config['configurations'][config_files]
            content = InlineTemplate(configurations['content'],
                                                        configurations=configurations)
            xml_config=config_files.split('-',1)[1]
            File(format("{nifi_base_dir}/conf/{xml_config}.xml"),
                content=content,
                owner=params.nifi_user,
                group=params.nifi_user
                )
        
            
        File(format("{nifi_base_dir}/conf/nifi.properties"),
            content=Template(
             "nifi.properties.j2"),
            owner=params.nifi_user,
            group=params.nifi_user
         )
        
        File(format("{nifi_base_dir}/conf/bootstrap.conf"),
            content=Template(
             "bootstrap.conf.j2"),
            owner=params.nifi_user,
            group=params.nifi_user
         )
        File(format("{nifi_base_dir}/conf/zookeeper.properties"),
            content=Template(
             "zookeeper.properties.j2"),
            owner=params.nifi_user,
            group=params.nifi_user
         )
        File(format("{nifi_base_dir}/bin/nifi-env.sh"),
            content=Template(
             "nifi-env.sh.j2"),
            owner=params.nifi_user,
            group=params.nifi_user,
            mode=0755
         )
        # Ensure all files owned by nifi user
        cmd = format("chown -R {nifi_user}:{nifi_group} {nifi_base_dir}")
        Execute(cmd)

        Execute('echo "Configuration complete"')

    def stop(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        stop_cmd = format("{nifi_base_dir}/bin/nifi.sh stop")
        print 'Stop the Master'
        Execute(stop_cmd)

    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)

        self.configure(env)
        start_cmd = format("{nifi_base_dir}/bin/nifi.sh start")
        print 'Start the Nifi'
        Execute(start_cmd)

    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("pgrep nifi")
        code, output = shell.call(status_cmd,timeout=10)
        if code == 0:
            Logger.info('Nifi is up and running')
        else:
            Logger.debug('Nifi is not running')
            raise ComponentIsNotRunning()

    def restart(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        restart_cmd = format("{nifi_base_dir}/bin/nifi.sh restart")
        print 'Restarting the Nifi'
        Execute(restart_cmd)



if __name__ == "__main__":
    Master().execute()

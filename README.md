# bcr-ambari-stack

Custom Ambari stack for BigData Services. This repo includes some of the custom service made for ambari services. This is not supported by Hortonworks.

# Prerequisit

You need to have Ambari server installed. This package works with both HDF and HDP. You should have access to the ambari server linux box.

# Supported Platform

1. CentOS/RHEL 7
2. Ambari 2.x
3. HDP/HDF

# Installation

Installing HDF 3.0 if you dont have it already

```
wget https://s3.amazonaws.com/public-repo-1.hortonworks.com/HDF/centos7/3.x/updates/3.0.2.0/tars/hdf_ambari_mp/hdf-ambari-mpack-3.0.2.0-76.tar.gz /tmp
ambari-server install-mpack --mpack=/tmp/hdf-ambari-mpack-3.0.2.0-76.tar.gz --purge --verbose
```

```
cd /var/lib/ambari-server/resources/
git clone https://github.com/becloudready/bcr-ambari-stack.git

```
Check what version of HDF or HDP is intalled in your system. Example of installing on HDP

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo ln -s /var/lib/ambari-server/resources/ambari-nifi /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/APACHENIFI
```

# Issues

Please raise issue with full logs and step to reproduce.


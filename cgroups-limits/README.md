[![pipeline status](https://bc2-gl.bc2.unibas.ch/ansible/ansible-roles/scicore-cgroups-limits/badges/master/pipeline.svg)](https://bc2-gl.bc2.unibas.ch/ansible/ansible-roles/scicore-cgroups-limits/commits/master)


scicore-cgroups-limits
=========

set cgroup limit (by default ON on the login node, OFF on the compute nodes)

Role Variables
--------------
```
cgroup_memory_limit_in_bytes: '10G'

to_whom_the_limit_applies: '@SCICORE-cluster-users'
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: scicore-cgroups-limits }

License
-------

GPLv3

Author Information
------------------

mj

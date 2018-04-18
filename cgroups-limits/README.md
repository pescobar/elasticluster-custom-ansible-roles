scicore-cgroups-limits
=========

set cgroup limit (by default ON on the login node, OFF on the compute nodes)

Role Variables
--------------
```
cgroup_memory_limit_in_bytes: '10G'

to_whom_the_limit_applies: '@course'
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: cgroups-limits }

License
-------

GPLv3

Author Information
------------------

mj

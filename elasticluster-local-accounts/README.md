# scicore-local-accounts

Add local accounts and groups.

Also add public ssh keys to the created accounts (optional)

For this role to work it's mandatory to define these variables:
- homes_folder
- users_to_create
- groups_to_create

If you don't override those variables the role will exit.

See [defaults/main.yml](defaults/main.yml) for details about how to define 
all the required variables *(you should never modify defaults/main.yml)*

## Dependencies

none

## Example of how to use this role in a playbook

```
  vars:

    homes_folder: /home

    groups_to_create:
      - group_name: group22
        group_gid: 345

    users_to_create:
      - username: user33
        group: group22
        uid: 987
        shell: /bin/bash
        password: $6$r.fuUgfjIm5O1d$CrXH.9pRuDbG9fpf74uKVPSdYvIZ00NK6FUQregvPMoA1q8Ggavd4qxaQReN25dJJnMptyYfx6OUv5nzC/5US1
        generate_ssh_key: yes

    ssh_keys_to_add:
      - username: user33
        ssh_keys: 
          - "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAsspNp9Xc9aU9l+OefjZQANWgozP3rgsKTJHfYxMELU42nLv/m6HhCL92XgyuP8eoWAfebqQU1KbIMZ3ZmZgpZeZQAU3wL9WsJ1asO7JJEUQ4m/7CaMQ+v6TRYD2YiUYxtOEQqpzIODeAjX2Uyj9ck7lue4yYbvuSaP3PdZ13XUGAXN7zTwUw54KWWjHBmZi07I953If0F6shmwdDpvc2PDePY6Lherp7i23YPd8NhZwxtzCXtvraNogGPflpLngCewpc4Vgttx4IFtwb2gy+npUCm7HzLdgESPE82oOAIpUkurLCwylDTEK8te44LMHeSVasJXRIrqKy1UKBOIYqVQ== haasj@bc2-login04.bc2.unibas.ch"
          - "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApXSS4Az11J/gwdvjB5XqdjCkD+go2BdJMtRsXfS7G0OyFAiuUyjNaP++e7qILWMkxfoKP6wIb5fWRq2nw9HYo52YmLaLLOECkz0CRHn0vo6J8K72itlXEc+GrWk7asNAvivr0YkP5Dl8MFK2cNwmdaYkdCKnqLesGmmODC20j4FPjtCUruL/HB1r4LjQY8kFy0GH/EnCKGQdKfJN52Mgabtp5pf0IVVBM9LCIYA3TDvk512zqJDPkwKqMmID+CiubxZUjeSXMg/EQqb31Dt/cxJiNZOAst005S5lY7WYtZWvFWy5GTKRbbZ0TDnvopO3rW2yKvDP4ScDa+hxdk5b7Q== gumiennr@login10.cluster.bc2.ch"
```          


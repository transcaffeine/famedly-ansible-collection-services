Role Name
=========

Role installs a [Ghost](https://ghost.org/) blog engine in Docker container

Requirements
------------

Target host should have Docker container engine running

Role Variables
--------------

Please check [default variables](./defaults/main.yml).

You can add your email config as follows:
```
blog_env_extra: 
  mail__transport: SMTP
  mail__from: "'Example Blog' <info@example.com>"
  mail__options__host: 127.0.0.1
  mail__options__port: 2525
blog_container_labels: {}
```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Brought to you by [AboveOps](https://aboveops.com) team

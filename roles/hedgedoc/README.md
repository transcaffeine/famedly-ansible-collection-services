# `famedly.services.hedgedoc` ansible role

Deploys a containerised HedgeDoc instance with postgres as the default backend.

## Requirements

- preconfigured postgresql database, f.ex. with `famedly.base.postgresql_client_access`
- docker daemon running, used for the deployment

## Role Variables

See `defaults/main.yml` and `vars/main.yml` for available variables.

## Example Playbook

```yaml
- hosts: your-server-name
  become: yes
  collections:
  roles:
    - famedly.internal.hedgedoc
  vars:
    hedgedoc_domain: "hedgedoc.example.org"
    hedgedoc_session_secret: "{{ vault_hedgedoc_session_secret }}"
    hedgedoc_config:
      allowEmailRegister: false
    hedgedoc_db_host: "your postgres host"
    hedgedoc_db_password: "s3cr3t"
```

## License

AGPL-3.0-only

## Author Information

- Jan Christian Grünhage <jcgruenhage@famedly.com>

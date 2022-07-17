# `famedly.services.snipe-it` ansible role

Deploys [snipe-it](https://snipeitapp.com/) in a
[docker container](https://snipe-it.readme.io/docs/docker)
and optionally a maria-db instance for storage.

## Requirements

The role assumes a docker host is running on the target.

## Configuration

Note that host directories for persistent storage in `snipe_it_base_path` need
to be owned by uid=1000, as the container creates and uses that userid.

The `snipe_it_config_app_key` needs to be generated using `php artisan key:generate --show`
in the running container, and then manually populated again using the role.

It is likely that symfony will not pick up the correct scheme from `snipe_it_config_app_url`,
for unknown reasons (correct `X-Forwarded-Proto`, `https` in app url, source IP in
`snipe_it_config_app_trusted_proxies`). In this case, setting `APP_FORCE_TLS`
in `snipe_it_config` will likely fix the issue.

## Role Variables

|  Name                                 |  Default value  | Description                                  |
|---------------------------------------|-----------------|----------------------------------------------|
| `snipe_it_config_app_key`             | `~`             | Laraval app key                              |
| `snipe_it_config_app_url`             | `~`             | URL where snipeit runs                       |
| `snipe_it_config_app_trusted_proxies` | `~`             | Where your reverse proxies run               |
| `snipe_it_config_db_username`         | `"snipe-it"`    | Username for the mariaDB                     |
| `snipe_it_config_db_password`         | `~`             | Password for the mariaDB                     |
| `snipe_it_config_db_host`             | `"snipeit-db"`  | Hostname of the mariaDB[¹]                   |
| `snipe_it_builtin_database_enable`    | `True`          | If the role should deploy a mariadb instance |

¹ Used as the container name for the built-in maria DB

## License

AGPL-3.0-only

## Author Information

- Johanna Dorothea Reichmann <j.reichmann@famedly.com>

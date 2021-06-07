# `famedly.internal.snipe-it` ansible role

Deploys [snipe-it](https://snipeitapp.com/) in a
[docker container](https://snipe-it.readme.io/docs/docker)
and optionally a maria-db instance for storage.

## Requirements

- docker

## Role Variables

|| Name                                 || Default value || Description                                 ||
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

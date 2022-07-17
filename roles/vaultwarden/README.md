# `famedly.services.vaultwarden' ansible role

Installs vaultwarden, a self-hosted bitwarden server implementation, using docker.

## Prerequisites

It is assumed the target host has a running docker daemon which can be used to
deploy the container, a user called `vaultwarden_user` may be created and
the `vaultwarden_config_dir` is writeable.

## Configuration

Overwrite the default `vaultwarden_docker_labels: {}` if you are
routing your traffic based on labels (e.g.: traefik, nginx-proxy-manager)


## License

GNU Affero General Public License v3

## Author Information

Famedly GmbH, famedly.de

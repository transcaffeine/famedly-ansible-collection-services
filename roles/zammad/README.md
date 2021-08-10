# Zammad-dockerized ansible role
This role is used to deploy the (experimental) version of [zammad](https://zammad.org) in docker containers.
The official repo uses docker-compose, the role skips docker-compose and interfaces with the docker daemon directly. It does pretty much the same thing docker-compose would do.

## Usage
Just execute the role as **root** (`become: yes`) and set at least these variables:
```yml
zammad_postgres_passwd: "super_secret_password"
zammad_host_network: "bridge" (Name of your hosts docker network, usually "bridge")
```
After running the role (which will take some time) you can access the Zammad-WebUi via port `8080` on the `zammad-nginx` container.
You may also use a reverse proxy or something similar. traefik for example.

## Containers
All containers are defined in `zammad_containers` by default these containers exist:
- zammad-postgresql
- zammad-memcached
- zammad-elasticsearch
- zammad-websocket
- zammad-railsserver
- zammad-scheduler
- zammad-backup
- zammad-init
- zammad-nginx

They are created/started in the same order as they are listed here. By default, all containers are added to the `zammad` docker-network. 

## Additional configuration
### Container labels
You can modify the container labels with `zammad_labels.[container_name]`. For Example:
```yml
zammad_labels:
  nginx:
    traefik.enable: "true"
    ...
```

### Host network
You may allow certain containers access to you hosts default network:
```yml
zammad_allow_host_nework:
  scheduler: yes
  railsserver: yes
```
You have to set `zammad_host_network` accordingly:
```yml 
zammad_host_network:
  name: "bridge"
```

### Add containers to the host network
Only containers in the `zammad_allow_host_nework` list are added to the host-network. Set it up like this:
```yml
zammad_allow_host_nework:
  scheduler: yes
  railsserver: yes
```

### Zammad internal network
You can customize the internal network with `zammad_network`, these are the defaults:
```yml
zammad_network:
  name: "zammad"
```

### http(s) port
The port can be set using `zammad_config_port`, default is `8080`

### Zammad user
The role creates a system use under which all zammad containers run. You can change the username with `zammad_user`

### Zammad paths
The following paths are used, these are the defaults:
```yml
zammad_base_path: /opt/zammad
zammad_command_dir: /usr/bin/
```

### `zammad-docker` command
This is a small command line utility that runs `sudo docker $1` for all zammad-containers.
You can disable this tool by setting `zammad_enable_command` to `no`.

### Postgres
Set the postgres user and password, you should use something like the ansible-vault for passwords:
```yml
zammad_postgres_user: "zammad" (by default same as zammad_user)
zammad_postgres_passwd: "super_secret_password"
```
#### Faked `/etc/passwd`
For security reasons the postgres container is not run as `root` (unless you run everything as `root` see Zammad user). Postgres requires access to `etc/passwd` (see https://hub.docker.com/_/postgres/). As it's unsecure to map the hosts passwd-file into the container, a fake `/etc/passwd` is created. This file only contains the necessary information for postgres to work.

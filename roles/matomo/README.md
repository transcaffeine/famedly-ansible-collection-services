Matomo
=========

Deploy Matomo (including redis and mariadb) using docker.

**warning: This role is currently unmaintained**
=======================================

Requirements
------------

You need docker and the docker python library installed on your host.

Role Variables
--------------

Look into the defaults file.
matomo_db_password: ""
redis_version: "5.0.5"
mariadb_version: "10.4.6"
matomo_version: "3.13.5"
matomo_http_host: "example.com"

License
-------

AGPLv3

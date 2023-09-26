Role Name
=========

This role deploys a simple murmur container. Murmur is the server for Mumble.

**warning: This role is currently unmaintained**
=======================================

Requirements
------------

This role uses a docker image to deploy the Murmur server. Docker has to be installed on the Target host and the murmur-docker repository must be reachable.

Role Variables
--------------

murmur_docker_ports: describes the port inside and outside the docker image
murmur_base_path: where murmur is installed to


Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: murmur-server
      roles:
         - murmur

License
-------

GNU Affero General Public License v3

Author Information
------------------

Famedly GmbH, famedly.de

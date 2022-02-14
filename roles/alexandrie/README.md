# `famedly.services.alexandrie` ansible role

This ansible role deploys [alexandrie](https://hirevo.github.io/alexandrie/),
a crate registry which features an optional web frontend and a rich API,
using a `docker` container.

## Usage

### Crate index

The [crate index](https://hirevo.github.io/alexandrie/concepts/crate-index.html)
is a `git` repository which is used as a metadata store for all crates the
registry manages.

As this inevitably requires a configured `git`, which is done by configuring:
```yaml
# alexandrie will use the following information when creating commits
alexandrie_git_author_name: Alexandrie Crate Registry
alexandrie_git_author_email: "alexandrie@my-company.tld"
# alexandrie will push it's branch to this configured remote:
alexandrie_git_remote_user: alexandrie
alexandrie_git_remote_pass: your-git-remote-credentials
alexandrie_git_remote_host: git.my-company.tld
alexandrie_git_remote_path: company-org/crate-index.git
```

*Warning*: The role currently assumes git-over-`https` with `BasicAuth`!

### Crate store

The [crate storage](https://hirevo.github.io/alexandrie/concepts/crate-storage.html)
is the place where the actual crates (code, assets, etc) are stored, so this place
needs to have enough storage and, if wanted, speed.

The simplest option is to store it locally on disk:
```yaml
# For disk storage, do not forget to mount that path in the container
# Defaults to "{{ alexandrie_base_path }}/crate-storage"
alexandrie_crate_storage_path: /path/to/fast/and/large/disk
alexandrie_container_volumes:
  - "/mnt/ssd-pool/alexandrie/:/path/to/fast/and/large/disk/:z"
```

Alexandrie supports an `s3`-compatible object storage server, though this is not
yet supported in this ansible role.

### Database

This role is meant for a deployment including a `postgresql` database, which
can be configured by populating the `alexandrie_database_[user|pass|name|host]`
variables.

### Authentication

When using external authentication methods, it is required to set
`alexandrie_domain` to the *domain* that alexandrie is reachable at,
and is used in `alexandrie_uri` with the default value of
`https://{{ alexandrie_domain }}` to construct OAuth callback URLs etc.

Alexandrie supports external authentication using OAuth via github and gitlab:
```yaml
alexandrie_auth_gitlab_enable: true
alexandrie_auth_gitlab_origin: "https://<your-gitlab-instance-url>"
alexandrie_auth_gitlab_client_id: "<your-oauth2-client-id>"
alexandrie_auth_gitlab_client_secret: "<your-auth2-client-secret>"
alexandrie_auth_gitlab_allow_registration: true
alexandrie_auth_gitlab_allowed_groups:
  - 'my-company/backend-team'
  - 'my-company/ops-team'
  - 'partner-company/project-team'
# For GitHub, the configuration is similar except the `origin` is
# always https://github.com
```

### Web Frontend

If the web-fronted is enabled, `alexandrie_frontend_session_secret` needs to be set.

## License

[AGPL-3.0-only](https://www.gnu.org/licenses/agpl-3.0.txt)

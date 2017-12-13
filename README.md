Stouts.sentry
============= 
[![Build Status](http://img.shields.io/travis/Stouts/Stouts.sentry.svg?style=flat-square)](https://travis-ci.org/Stouts/Stouts.sentry)
[![Galaxy](http://img.shields.io/badge/galaxy-Stouts.sentry-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/935)

Ansible role which install and setup [Sentry](https://getsentry.com)

#### Recomended

- [Stouts.nginx](https://github.com/Stouts/Stouts.nginx)
- [Stouts.docker](https://github.com/Stouts/Stouts.python)
- [Stouts.postfix](https://github.com/Stouts/Stouts.postfix)


#### Variables

The role variables and default values.

```yaml
sentry_enabled: true                                        # Enable the role
sentry_version: 8.22
sentry_secret_key: replaceme                                # Setup secret key for Sentry installation

sentry_home: /opt/sentry
sentry_hostname: "{{inventory_hostname}}"
sentry_single_organization: true

sentry_plugins: []                                          # Setup plugins
sentry_config_additional: []                                # List of additional options

# Postgresql
sentry_postgres_host: postgres
sentry_postgres_port: ""
sentry_db_name: postgres
sentry_db_user: postgres
sentry_db_password: postgres
sentry_db_options: {autocommit: 1}

# Redis
sentry_redis_host: redis
sentry_redis_password: ""
sentry_redis_db: 0
sentry_redis_port: 6379

# Memcached
sentry_memcached_host: memcached
sentry_memcached_port: 11211

# AMPQ
sentry_broker_url: "redis://{{sentry_redis_host}}:{{sentry_redis_port}}"

# Filestorage
sentry_filestore_location: "{{sentry_home}}/files"
sentry_filestore_backend: "filesystem"
sentry_filestore_access_key: ""
sentry_filestore_secret_key: ""
sentry_filestore_bucket_name: ""


# SSL
sentry_use_ssl: false
sentry_nginx: true
sentry_nginx_port: 80
sentry_nginx_ssl_redirect: "{{sentry_use_ssl}}"                 # 80 -> 443
sentry_nginx_ssl_certificate:                                   # SSL certificate file - also turns on HTTPS on Nginx
sentry_nginx_ssl_certificate_key:                               # Key file for SSL cert
sentry_nginx_timeout: 15s
sentry_nginx_body_size: 150k
sentry_nginx_access_log: /var/log/sentry-access.log
sentry_nginx_error_log: /var/log/sentry-error.log

# Emails
sentry_mail_backend: smtp
sentry_mail_enable_replies: false
sentry_mail_from: "sentry@{{sentry_hostname}}"         # From email
sentry_mail_host: localhost
sentry_mail_reply_hostname: ""
sentry_mail_password: ""
sentry_mail_port: 25
sentry_mail_use_tls: false
sentry_mail_username: ""
sentry_mail_mailgun_api_key: ""

# Social auth settings
sentry_twitter_consumer_key: ""
sentry_twitter_consumer_secret: ""
sentry_facebook_app_id: ""
sentry_facebook_api_secret: ""
sentry_google_oauth2_client_id: ""
sentry_google_oauth2_client_secret: ""
sentry_github_app_id: ""
sentry_github_api_secret: ""
sentry_trello_api_key: ""
sentry_trello_api_secret: ""
sentry_bitbucket_consumer_key: ""
sentry_bitbucket_consumer_secret: ""

# Web
sentry_web_host: 127.0.0.1
sentry_web_port: 9000
sentry_web_options: {}

# Setup docker containers
sentry_redis: true
sentry_postgres: true
sentry_memcached: true

# Initial users
sentry_admins:
  - email: "admin@{{sentry_hostname}}"
    password: "admin"

sentry_auth_register: false
sentry_beacon: true
```

#### Usage

Add `Stouts.sentry` to your roles and set vars in your playbook file.

Example:

```yaml

- hosts: all
  sudo: true

  roles:
  - Stouts.python
  - Stouts.docker
  - Stouts.nginx
  - Stouts.sentry

```

#### License

Licensed under the MIT License. See the LICENSE file for details.

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Stouts/Stouts.sentry/issues)!

If you wish to express your appreciation for the role, you are welcome to send
a postcard to:

    Kirill Klenov
    pos. Severny 8-3
    MO, Istra, 143500
    Russia

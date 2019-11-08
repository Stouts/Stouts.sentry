# This file was generated by Ansible for {{ ansible_fqdn }}
# Do NOT modify this file by hand!

from sentry.conf.server import *

import os.path

# Directories
CONF_ROOT = os.path.dirname(__file__)

# Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'sentry.db.postgres',
        'NAME': '{{sentry_db_name}}',
        'USER': '{{sentry_db_user}}',
        'PASSWORD': '{{sentry_db_password}}',
        {% if sentry_postgres_host %}'HOST': '{{sentry_postgres_host}}',{% endif %}
        {% if sentry_postgres_port %}'PORT': '{{sentry_postgres_port}}',{% endif %}
        'OPTIONS': {{sentry_db_options|to_nice_json}}
    }
}

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = True

###########
# General #
###########

# Instruct Sentry that this install intends to be run by a single organization
# and thus various UI optimizations should be enabled.
SENTRY_SINGLE_ORGANIZATION = {{sentry_single_organization and 'True' or 'False'}}

#########
# Cache #
#########

# Sentry currently utilizes two separate mechanisms. While CACHES is not a
# requirement, it will optimize several high throughput patterns.


# A primary cache is required for things such as processing events
SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

{% if sentry_memcached_host %}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['{{sentry_memcached_host}}:{{sentry_memcached_port}}'],
        'TIMEOUT': 3600,
    }
}
{% endif %}

#########
# Queue #
#########

# See https://docs.getsentry.com/on-premise/server/queue/ for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

BROKER_URL = '{{sentry_broker_url}}'

###############
# Rate Limits #
###############

# Rate limits apply to notification handlers and are enforced per-project
# automatically.

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

##################
# Update Buffers #
##################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

##########
# Quotas #
##########

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

########
# TSDB #
########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

###########
# Digests #
###########

# The digest backend powers notification summaries.

SENTRY_DIGESTS = 'sentry.digests.backends.redis.RedisBackend'


##############
# Web Server #
##############

# If you're using a reverse SSL proxy, you should enable the X-Forwarded-Proto
# header and set `SENTRY_USE_SSL=1`

{% if sentry_use_ssl %}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
{% endif %}

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {{sentry_web_options|to_nice_json}}

#  Social
TWITTER_CONSUMER_KEY = '{{sentry_twitter_consumer_key}}'
TWITTER_CONSUMER_SECRET = '{{sentry_twitter_consumer_secret}}'
FACEBOOK_APP_ID = '{{sentry_facebook_app_id}}'
FACEBOOK_API_SECRET = '{{sentry_facebook_api_secret}}'
GOOGLE_OAUTH2_CLIENT_ID = '{{sentry_google_oauth2_client_id}}'
GOOGLE_OAUTH2_CLIENT_SECRET = '{{sentry_google_oauth2_client_secret}}'
GITHUB_APP_ID = '{{sentry_github_app_id}}'
GITHUB_API_SECRET = '{{sentry_github_api_secret}}'
GITHUB_EXTENDED_PERMISSIONS = ['repo']
TRELLO_API_KEY = '{{sentry_trello_api_key}}'
TRELLO_API_SECRET = '{{sentry_trello_api_secret}}'
BITBUCKET_CONSUMER_KEY = '{{sentry_bitbucket_consumer_key}}'
BITBUCKET_CONSUMER_SECRET = '{{sentry_bitbucket_consumer_secret}}'

{% if not sentry_auth_register %}
SENTRY_FEATURES['auth:register'] = False
{% endif %}

{% if sentry_beacon %}
SENTRY_BEACON = True
{% endif %}

#####################
# SLACK INTEGRATION #
#####################
slack = env('SLACK_CLIENT_ID') and env('SLACK_CLIENT_SECRET')
if slack:
    SENTRY_OPTIONS['slack.client-id'] = env('SLACK_CLIENT_ID')
    SENTRY_OPTIONS['slack.client-secret'] = env('SLACK_CLIENT_SECRET')
    SENTRY_OPTIONS['slack.verification-token'] = env('SLACK_VERIFICATION_TOKEN') or ''

# Additional settings
{% for option in sentry_config_py or [] %}
{{option}}
{% endfor %}

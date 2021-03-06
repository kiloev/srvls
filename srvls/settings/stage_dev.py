from .base import *  # noqa: F401 F403
from .base import AWS_STORAGE_BUCKET_NAME


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'db.sqlite3',
        'BUCKET': AWS_STORAGE_BUCKET_NAME
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)-8s] %(message)s'
        }
    },
    'handlers': {
        'cloudwatch': {
            'class': 'watchtower.CloudWatchLogHandler',
            'log_group': f'{AWS_STORAGE_BUCKET_NAME}-logs',
            'use_queues': False,
            'formatter': 'simple'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['cloudwatch']
        }
    },
}

STATICFILES_STORAGE = 'srvls.aws.StaticStorage'
DEFAULT_FILE_STORAGE = 'srvls.aws.MediaStorage'
MEDIA_ROOT = '/tmp/media/'
STATIC_ROOT = '/tmp/static/'

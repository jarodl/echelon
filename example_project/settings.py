import os.path

ECHELON_ROOT = os.path.dirname(__import__('echelon').__file__)

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'echelon.sqlite'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',

    'devserver',
    'echelon',
    'south',
)

ADMIN_MEDIA_PREFIX = '/admin/media/'

ROOT_URLCONF = 'urls'

DEVSERVER_MODULES = ()

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ECHELON_ROOT, 'templates', 'echelon'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'echelon.context_processors.default',
    'echelon.context_processors.root_categories',
    'echelon.context_processors.settings',
)

try:
  from local_settings import *
except ImportError:
  pass

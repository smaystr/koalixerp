'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .common import *  # noqa

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
# Commenting this line because the settings file for mezzanine differs from
# Django 1.8 dictionary structure.
# TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# Mail settings
# -----------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# CACHING
# -----------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ('127.0.0.1',)


# This is a last-ditch-effort move,
# you shouldn't have to do this,
# but it will clearly show if there's merely some configuration issue
# or whether there's some larger issue.
def show_toolbar(request): return True


DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
CRISPY_FAIL_SILENTLY = not DEBUG

# django-extensions
# -----------------------------------------------------------------------------
# OPTIONAL APPLICATIONS
# These will be added to ``INSTALLED_APPS``, only if available.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
INSTALLED_APPS += (
    "debug_toolbar",
    "django_extensions",
    'autofixture',
    PACKAGE_NAME_FILEBROWSER,
)
# TESTING
# -----------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']

DATABASES['default']['NAME'] = ''
DATABASES['default']['USER'] = ''
DATABASES['default']['PASSWORD'] = ''
DATABASES['default']['HOST'] = ''
DATABASES['default']['PORT'] = ''

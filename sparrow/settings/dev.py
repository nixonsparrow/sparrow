from .base import *
import mimetypes

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&wmh+f2#u*p^y8#ugnf*0*e$%2m0$acip6+0p^$!cr*s_fkuy)'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
] + MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1', '172.17.0.1']

# SHOW_TOOLBAR_CALLBACK = True

mimetypes.add_type("application/javascript", ".js", True)

try:
    from .local import *
except ImportError:
    pass

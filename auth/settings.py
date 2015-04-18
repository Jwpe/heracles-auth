import dj_database_url
import datetime
import os
from path import path

PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
os.sys.path.insert(0, PROJECT_ROOT / 'apps')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('PRIMARY_DATABASE_URL')),
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Third party
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'auth.handlers.auth_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000),
}

ROOT_URLCONF = 'auth.urls'

if os.environ.get('DEVELOPMENT'):
    DEBUG = True
else:
    DEBUG = False

### Environment variables
# Classic Django secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

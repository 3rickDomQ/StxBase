# Own's Libraries
from .base import deploy
from .base import directories
from .base import applications
from .base import logs
from .base import database
from .base import media
from .base import templates
from .base import security
from .base import internationalization
from .base import statics
from .base import messages
from .base import rest


# App configuration
APP_CLAVE = "AVD"
APP_NAME = "PANDO"
APP_YEAR_RELEASE = "2020"
APP_VERSION = "0.0.1"

JET_DEFAULT_THEME = 'light-blue'

SECRET_KEY = deploy.SECRET_KEY
ROOT_URLCONF = deploy.ROOT_URLCONF
WSGI_APPLICATION = deploy.WSGI_APPLICATION
ALLOWED_HOSTS = deploy.ALLOWED_HOSTS
DEBUG = deploy.DEBUG

INSTALLED_APPS = applications.get_InstalledApps()

LOGGING = logs.get_Config(
    deploy.Enviroment.LOCAL,
    directories.LOCAL_LOG_PATH
)

DATABASES = database.get_Config(APP_CLAVE, deploy.Enviroment.LOCAL)

MIDDLEWARE = security.get_Middlewares()

TEMPLATES = templates.get_Config(directories.TAGS)

AUTH_USER_MODEL = security.AUTH_USER_MODEL
AUTH_PASSWORD_VALIDATORS = security.AUTH_PASSWORD_VALIDATORS
SESSION_EXPIRE_SECONDS = security.SESSION_EXPIRE_SECONDS
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = security.SESSION_EXPIRE_AFTER_LAST_ACTIVITY
SESSION_EXPIRE_AT_BROWSER_CLOSE = security.SESSION_EXPIRE_AT_BROWSER_CLOSE

MESSAGE_TAGS = messages.TAGS

LANGUAGE_CODE = internationalization.LANGUAGE_CODE
USE_I18N = internationalization.USE_I18N
TIME_ZONE = internationalization.TIME_ZONE
USE_TZ = internationalization.USE_TZ
USE_L10N = internationalization.USE_L10N
DATE_INPUT_FORMATS = internationalization.DATE_INPUT_FORMATS
DATETIME_INPUT_FORMATS = internationalization.DATETIME_INPUT_FORMATS
USE_THOUSAND_SEPARATOR = internationalization.USE_THOUSAND_SEPARATOR
THOUSAND_SEPARATOR = internationalization.THOUSAND_SEPARATOR
NUMBER_GROUPING = internationalization.NUMBER_GROUPING
DECIMAL_SEPARATOR = internationalization.DECIMAL_SEPARATOR

# AWS settings
# AWS_ACCESS_KEY_ID = aws.AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY = aws.AWS_SECRET_ACCESS_KEY
# AWS_DEFAULT_ACL = aws.AWS_DEFAULT_ACL
# AWS_QUERYSTRING_AUTH = aws.AWS_QUERYSTRING_AUTH
# AWS_S3_OBJECT_PARAMETERS = aws.AWS_S3_OBJECT_PARAMETERS

# AWS_STORAGE_BUCKET_NAME = aws.get_FilesBucketName(APP_CLAVE, deploy.Enviroment.DEVELOPMENT)
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_STATIC_LOCATION = aws.AWS_STATIC_LOCATION

#  Static settings
STATIC_URL = '/static/'
# STATIC_URL = 'http://127.0.0.1:9001/'
STATIC_ROOT = directories.STATIC_ROOT
STATICFILES_DIRS = directories.STATICFILE_DIRS
STATICFILES_FINDERS = statics.STATICFILES_FINDERS
# STATICFILES_STORAGE = statics.STATICFILES_STORAGE

#  Media settings
MEDIA_URL = media.MEDIA_URL
MEDIA_ROOT = directories.MEDIA_ROOT
FILE_UPLOAD_PERMISSIONS = media.FILE_UPLOAD_PERMISSIONS
# DEFAULT_FILE_STORAGE = media.DEFAULT_FILE_STORAGE
# PRIVATE_FILE_STORAGE = media.PRIVATE_FILE_STORAGE

# Rest Settings
CORS_ORIGIN_ALLOW_ALL = rest.CORS_ORIGIN_ALLOW_ALL
REST_FRAMEWORK = rest.REST_FRAMEWORK

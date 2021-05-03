import enum


class Enviroment(enum.Enum):
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"
    DEVELOPMENT = "DEVELOPMENT"
    LOCAL = "LOCAL"


SECRET_KEY = '#=#rkazc2&sj!5-khata3s2s81$6mgfv&)amdwtuu!myjeop3+'

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

ALLOWED_HOSTS = ['*', ]

DEBUG = True


def get_Middlewares():
    middlewares = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'Utils.middlewares.SessionControlMiddleware',
        'Utils.middlewares.OnlyOneSessionMiddleware'
    ]

    return middlewares


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
    {
        'NAME': 'Utils.validators.HasUpperCaseValidator',
    },
    {
        'NAME': 'Utils.validators.HasSpecialCharacterValidator',
    },
    {
        'NAME': 'Utils.validators.HasNumberValidator',
    }
]

# SESSION_EXPIRE_SECONDS = 60
SESSION_EXPIRE_SECONDS = 9000
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Security Configuration
AUTH_USER_MODEL = 'core.User'
PASSWORD_LIMIT_DAYS = 90
LOGIN_URL = 'backoffice:login'
LOGOUT_REDIRECT_URL = 'backoffice:login'

DEFAULT_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'simple_history',
    'storages',
    'Utils.apps.UtilsConfig',
    'widget_tweaks'
]

OWN_DATA_APPS = [
    'core.apps.CoreConfig',
]

OWN_BUSINESS_APPS = [
    'Business.apps.BusinessConfig',
]

OWN_WEBSITE_APPS = [
    'backoffice.apps.BackofficeConfig',
    'public.apps.PublicConfig'
]

OWN_WEBAPI_APPS = [
    'backoffice-api.apps.BackofficeApiConfig',
]


def get_InstalledApps():
    apps = DEFAULT_APPS + \
        THIRD_PARTY_APPS + \
        OWN_DATA_APPS + \
        OWN_BUSINESS_APPS + \
        OWN_WEBSITE_APPS + \
        OWN_WEBAPI_APPS

    return apps

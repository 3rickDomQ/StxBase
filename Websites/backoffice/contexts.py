# Django's Libraries
from django.conf import settings

# Own's Libraries
from Business.controllers import BackofficeWeb


def get_AppInfo(request):
    data = {
        'name': settings.APP_NAME,
        'version': settings.APP_VERSION,
        # 'partner_name': settings.APP_PARTNER_NAME,
        # 'year_release': settings.APP_YEAR_RELEASE,
    }
    return {'APP': data}


def get_UserInfo(request):
    user_data = BackofficeWeb.get_UserLoggedData(request, None)

    data = {
        'pk': user_data['pk'],
        'email': user_data['email'],
        'name': user_data['name'],
        'is_superuser': user_data['is_superuser'],
        'position_name': user_data['position_name'],
        'first_login': user_data['first_login'],
        'last_campaign_rol': user_data['last_campaign_rol'],
        'menu': user_data['menu']
    }
    return {'USER': data}

# Django's Libraries
from django.urls import path

# Third-party Libraries


app_name = "backoffice-api"

urlpatterns = [
    path(
        'users/',
        UsersApiView.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='users-api'
    ),
]

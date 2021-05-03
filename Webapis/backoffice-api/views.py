
# Third-party Libraries
from rest_framework import status
from rest_framework.response import Response

# Own's Libraries
from Utils.views_rest import SecurityListCreateApiView

from Business.controllers import BackofficeWeb

from .serializers import UserSerializer


class UsersApiView(SecurityListCreateApiView):
    app_class = BackofficeWeb
    serializer_class = UserSerializer
    list_method = "get_Users"
    create_method = "create_Ciudadano"

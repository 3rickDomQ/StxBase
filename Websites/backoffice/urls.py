# Django's Libraries
from django.urls import path
from django.urls import re_path



app_name = "backoffice"
SECURITY = [
]

CORE = [
]

CATALOGUES = [
]

PROCESS = [
]

urlpatterns = SECURITY + \
    CORE + \
    CATALOGUES + \
    PROCESS

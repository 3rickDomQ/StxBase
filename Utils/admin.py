# Django's Libraries
from django.contrib import admin
from django.conf import settings


# admin.site.disable_action('delete_selected')
admin.site.site_header = settings.APP_NAME

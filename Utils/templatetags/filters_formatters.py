# Python's Libraries
from datetime import datetime
# import locale

# Django's Libraries
from django import template

register = template.Library()


@register.filter
def date_format(value):
    # locale.setlocale(locale.LC_TIME, "es_ES.utf8")

    date_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
    str_date = date_obj.strftime("%d/%m/%Y %H:%M:%S")
    return str_date

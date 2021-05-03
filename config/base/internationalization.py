
# Internationalization
LANGUAGE_CODE = 'es-MX'
USE_I18N = True

TIME_ZONE = 'America/Mexico_City'
USE_TZ = True

USE_L10N = True
DATE_INPUT_FORMATS = ['%d/%m/%Y', ]
DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%M',
    '%d/%m/%Y %H:%M:%S',
]
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3
DECIMAL_SEPARATOR = '.'

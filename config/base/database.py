import os


def get_Config(_app_clave, _enviroment):
    if _enviroment.value == "PRODUCTION":
        return {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.getenv(f'PROD_{_app_clave}_DB_NAME'),
                'USER': os.getenv(f'PROD_{_app_clave}_DB_USER'),
                'PASSWORD': os.getenv(f'PROD_{_app_clave}_DB_PASS'),
                'HOST': os.getenv(f'PROD_{_app_clave}_DB_HOST'),
                'PORT': os.getenv(f'PROD_{_app_clave}_DB_PORT'),
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
            }
        }

    if _enviroment.value == "DEVELOPMENT":
        return {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.getenv(f'DEV_{_app_clave}_DB_NAME'),
                'USER': os.getenv(f'DEV_{_app_clave}_DB_USER'),
                'PASSWORD': os.getenv(f'DEV_{_app_clave}_DB_PASS'),
                'HOST': os.getenv(f'DEV_{_app_clave}_DB_HOST'),
                'PORT': os.getenv(f'DEV_{_app_clave}_DB_PORT'),
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
            },
        }

    if _enviroment.value == "LOCAL":
        return {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.getenv(f'LOCAL_{_app_clave}_DB_NAME'),
                'USER': os.getenv(f'LOCAL_{_app_clave}_DB_USER'),
                'PASSWORD': os.getenv(f'LOCAL_{_app_clave}_DB_PASS'),
                'HOST': os.getenv(f'LOCAL_{_app_clave}_DB_HOST'),
                'PORT': os.getenv(f'LOCAL_{_app_clave}_DB_PORT'),
            },
        }

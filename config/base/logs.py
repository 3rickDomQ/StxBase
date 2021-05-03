

def get_Config(_enviroment, _path):

    if _enviroment.value == "PRODUCTION":
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console': {
                    'format': '%(asctime)s [%(levelname)s] %(message)s',
                    'datefmt': '%d-%b-%y %H:%M:%S'
                },
                'file': {
                    'format': '%(asctime)s [%(levelname)s] %(message)s',
                    'datefmt': '%d-%b-%y %H:%M:%S'
                }
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'console'
                },
                'file': {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'formatter': 'file',
                    # 'filename': _path + "debug.log"
                    'filename': _path
                }
            },
            'loggers': {
                'app_logger': {
                    'handlers': ['file', 'console'],
                    'level': 'DEBUG',
                    'propagate': True
                }
            },
        }

    if _enviroment.value == "LOCAL":
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console': {
                    'format': '%(asctime)s [%(levelname)s] %(message)s',
                    'datefmt': '%d-%b-%y %H:%M:%S'
                },
                'file': {
                    'format': '%(asctime)s [%(levelname)s] %(message)s',
                    'datefmt': '%d-%b-%y %H:%M:%S'
                }
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'console'
                },
                'file': {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'formatter': 'file',
                    # 'filename': _path + "debug.log"
                    'filename': _path
                }
            },
            'loggers': {
                'app_logger': {
                    'handlers': ['file', 'console'],
                    'level': 'DEBUG',
                    'propagate': True
                },
                'django.db.backends': {
                    'handlers': ['file'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }

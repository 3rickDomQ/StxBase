

def get_Config(_tags_path):
    templates = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                _tags_path,
                # TEMPLATES
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'backoffice.contexts.get_AppInfo',
                    'backoffice.contexts.get_UserInfo'
                ],
            },
        },
    ]

    return templates

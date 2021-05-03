import os


# AWS SETTINGS
def get_AccessKeyId(_app_clave, _environment):
    if _environment.value == "PRODUCTION":
        value = os.getenv(f"PROD_{_app_clave}_AWS_ACCESS_KEY_ID")
        # import pdb; pdb.set_trace()
        return value

    if _environment.value == "DEVELOPMENT":
        value = os.getenv(f"DEV_{_app_clave}_AWS_ACCESS_KEY_ID")
        return value


def get_SecretAccessKey(_app_clave, _environment):
    if _environment.value == "PRODUCTION":
        # import pdb; pdb.set_trace()

        value = os.getenv(f"PROD_{_app_clave}_AWS_SECRET_ACCESS_KEY")
        return value

    if _environment.value == "DEVELOPMENT":
        value = os.getenv(f"DEV_{_app_clave}_AWS_SECRET_ACCESS_KEY")
        return value


AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_STATIC_LOCATION = "static"
AWS_PUBLIC_MEDIA_LOCATION = 'media'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'


# AWS Bucket
def get_FilesBucketName(_app_clave, _enviroment):
    if _enviroment.value == "PRODUCTION":
        value = os.getenv(f"PROD_{_app_clave}_AWS_BUCKET_NAME")
        return value

    if _enviroment.value == "DEVELOPMENT":
        value = os.getenv(f"DEV_{_app_clave}_AWS_BUCKET_NAME")
        return value


# AWS QuickSight
AWS_QS_ACCESS_KEY_ID = os.getenv('AWS_QS_ACCESS_KEY_ID')
AWS_QS_SECRET_ACCESS_KEY = os.getenv('AWS_QS_SECRET_ACCESS_KEY')
AWS_QS_REGION = 'us-east-1'

AWS_QS_ACCOUNT_ID = os.getenv('AWS_QS_ACCOUNT_ID')
AWS_QS_IDENTITY_TYPE = 'IAM'

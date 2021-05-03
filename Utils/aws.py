# Python's Libraries
import logging

# Third-party Libraries
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError


class AwsBucket(object):

    def __init__(
        self,
        _bucket_name,
        _key,
        _secret_key=None,
        _logger=None
    ):
        self.name = _bucket_name
        self.key = _key
        self.secret_key = _secret_key
        self.logger = _logger or logging.getLogger(__name__)

    def upload_File(self, _local_path, _aws_path):
        self.logger.debug("Subiendo archivo a bucket")

        client = boto3.client(
            's3',
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret_key
        )

        try:
            client.upload_file(
                Bucket=self.name,
                Filename=_local_path,
                Key=_aws_path
            )
            return True

        except FileNotFoundError:
            msg_error = "No se encuentra el archivo"
            self.logger.error(msg_error)
            raise NameError(msg_error)

        except NoCredentialsError:
            msg_error = "Credenciales incorrectas"
            self.logger.error(msg_error)
            raise NameError(msg_error)

    def get_Presigned_Url(self, _object, _expiration=3600):
        self.logger.info("--> Firmando Objeto del Bucket")
        client = boto3.client(
            's3',
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret_key
        )

        try:
            response = client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': self.name,
                    'Key': _object
                },
                ExpiresIn=_expiration
            )

            self.logger.info("<-- Objecto Firmado Correctamente")
            return response

        except ClientError as e:
            msg = f"<-- Fallo firma de objeto, {e}"
            self.logger.error(msg)
            raise ClientError(msg)

# Python's Libraries
import logging
from datetime import datetime
from datetime import timedelta

# Third-party Libraires
import jwt
from jwt.exceptions import InvalidSignatureError
from jwt.exceptions import ExpiredSignatureError

# Own's Libraries
from .errors import SecurityError


class SecurityJWT(object):

    def __init__(self, _secret, _exp=3600, _logger=None):
        self.secret = _secret
        self.expiration = _exp
        self.logger = _logger or logging.getLogger(__name__)

    def generate_TokenFromEmail(self, _email):
        self.logger.info("--> Generando Token")
        encoded_jwt = jwt.encode(
            {
                'email': _email
            },
            'secret',
            algorithm='HS256'
        )
        self.logger.info("<-- Token Generado")
        return encoded_jwt.decode()

    def validate_TokenByEmail(self, _token, _email):
        self.logger.info("--> Validando Token")

        try:
            payload = jwt.decode(_token, 'secret', algorithms=['HS256'])
            if payload['email'] == _email:
                self.logger.info("<-- Token Valido")
                return True
            else:
                msg = "<-- Información codificada incorrecta"
                self.logger.error(msg)
                raise SecurityError(msg)

        except InvalidSignatureError:
            msg = "<-- Token Invalido"
            self.logger.error(msg)
            raise SecurityError(msg)

        except Exception as e:
            msg = f"<-- Ocurrio problemas validando el token, {e}"
            self.logger.error(msg)
            raise SecurityError(msg)

    def generate_TokenFromDict(self, _dict):
        self.logger.info("--> Generando Token")
        _dict['exp'] = datetime.utcnow() + timedelta(seconds=self.expiration)
        encoded_jwt = jwt.encode(
            _dict,
            self.secret,
            algorithm='HS256'
        )
        self.logger.info("<-- Token Generado")
        return encoded_jwt.decode()

    def validate_AppraisalPDFToken(self, _token):
        self.logger.info("--> Validando Token")
        try:
            payload = jwt.decode(_token, self.secret, algorithms=['HS256'])

            if 'appraisal_id' not in payload:
                raise NameError("<-- Token Invalido: No se especifico ID de Solicitud")

            self.logger.info("<-- Token Valido")
            return payload

        except ExpiredSignatureError:
            msg = "<-- Token Invalido: Expirado"
            self.logger.error(msg)
            raise NameError(msg)

        except InvalidSignatureError:
            msg = "<-- Token Invalido: Firma invalida"
            self.logger.error(msg)
            raise NameError(msg)

    def generate_AppraisalPDFToken(self, _dict):
        self.logger.info("--> Generando Token")
        _dict['exp'] = datetime.utcnow() + timedelta(
            seconds=self.expiration
        )
        encoded_jwt = jwt.encode(
            _dict,
            self.secret,
            algorithm='HS256'
        )
        self.logger.info("<-- Token Generado")
        return encoded_jwt.decode()

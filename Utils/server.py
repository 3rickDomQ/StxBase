# Python's Libriares
import logging

# Django's Libraries
from django.core.exceptions import MultipleObjectsReturned
# from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.db import IntegrityError

# Third-party Libraries
import requests

# Own's Libraries
from Utils.errors import NoRecordFoundError
from Utils.errors import NoRecordsFoundError
from Utils.errors import MultipleRecordsFoundError
from Utils.errors import DataBaseError
from Utils.errors import ServerError
from Utils.errors import DuplicateEntryError

from Utils.data import Scribe

logger = logging.getLogger("app_logger")


class DataBase(object):
    """Clase con metodos para realizar distintas operaciones
    con la base de datos a partir de los modelos.
    """

    def __init__(self, _db_name="default", _logger=None):
        self.db_name = _db_name
        self.logger = _logger or logging.getLogger(__name__)

    def insert(self, _model):
        self.logger.info('... Insertando registro en Tabla.')

        try:
            _model.save()
            _model.full_clean()
            self.logger.info('... Registro insertado con exito.')
            return True

        except IntegrityError as e:
            msg = str(e)
            raise DuplicateEntryError(msg, _model, self.logger)

        except Exception as e:
            msg = str(e)
            raise DataBaseError(msg, _model, self.logger)

    def select_Many(
        self,
        _model,
        _prefetch_list=None,
        _custom_filters=None,
        _exclude=None
    ):
        self.logger.info('... Buscando registros en Tabla.')

        try:
            filters = Scribe.get_DicFromModel(_model, _primaries=True)

            if _prefetch_list:
                query = _model.__class__.objects.prefetch_related(
                    *_prefetch_list
                ).all()
            else:
                query = _model.__class__.objects.all()

            if hasattr(_model, "filter_obj"):
                filter_obj = _model.filter_obj
                if filter_obj.is_bound:
                    filter_obj.errors
                    query = filter_obj.filter_queryset(query)

            if bool(filters) is True:
                query = query.filter(**filters)

            if _custom_filters:
                query = query.filter(_custom_filters)

            if bool(_exclude) is True:
                query = query.exclude(**_exclude)

        except Exception as e:
            msg = str(e)
            raise DataBaseError(msg, _model, self.logger)

        qty_records = len(query)

        if qty_records == 0:
            msg = 'No se encontraron registros en la BD.'
            raise NoRecordsFoundError(msg, _model, self.logger)

        self.logger.info(f'... Se encontraron {qty_records} registros en la BD.')
        return query

    def select_One(
        self,
        _model,
        _prefetch_list=None,
        _custom_filters=None
    ):
        self.logger.info('... Buscando registro en Tabla.')

        filters = Scribe.get_DicFromModel(_model, _primaries=True)
        print(filters)

        if bool(filters) is False:
            msg = "No se especifico valor en ningún atributo."
            raise DataBaseError(msg, self.logger, _model)

        try:
            if _prefetch_list:
                if _custom_filters:
                    query = _model.__class__.objects.get(_custom_filters)

                else:
                    query = _model.__class__.objects.prefetch_related(
                        *_prefetch_list
                    ).get(**filters)

            else:
                if _custom_filters:
                    query = _model.__class__.objects.get(_custom_filters)

                else:
                    query = _model.__class__.objects.get(**filters)

            self.logger.info('... Registro encontrado con exito.')
            return query

        except _model.__class__.DoesNotExist:
            msg = "No se encontro el registro."
            raise NoRecordFoundError(msg, _model, self.logger)

        except MultipleObjectsReturned:
            msg = "Se encontro mas de un registro."
            raise MultipleRecordsFoundError(msg, _model, self.logger)

        except Exception as e:
            msg = str(e)
            raise DataBaseError(msg, _model, self.logger)

    def update(self, _model):
        self.logger.info('... Actualizando registro en Tabla.')

        try:
            _model.full_clean()
            _model.save()

            self.logger.info('... Registro actualizado con exito.')
            return True

        except Exception as e:
            msg = str(e)
            raise DataBaseError(msg, _model, self.logger)

    def delete(self, _model):
        self.logger.info('... Eliminando registro en Tabla.')
        try:
            _model.delete()
            self.logger.info('... Registro eliminado con exito.')
            return True

        except Exception as e:
            msg = str(e)
            raise DataBaseError(msg, _model, self.logger)


class Postman(object):

    def __init__(self, _email_backend):
        self.email_backend = _email_backend

    def send_Email(self, _from, _to, _subject, _body, _attach=None):
        email_message = EmailMultiAlternatives(
            _subject,
            _body,
            _from,
            to=_to,
            connection=self.email_backend
        )
        email_message.attach_alternative(_body, 'text/html')

        if _attach:
            email_message.attach_file(_attach)

        email_message.send()


class Connector(object):

    def __init__(self, _logger=None):
        self.logger = _logger or logging.getLogger(__name__)

    def _get_Headers(self, _token, _type):
        headers = {}
        if _token:
            if _type:
                headers = {
                    'Authorization': f'{_type} {_token}'
                }
            else:
                headers = {
                    'Authorization': _token
                }

        return headers

    def get(self, _url, _token=None, _type="Bearer"):
        """Metodo interno que encarga de realizar el request al Servidor

        :param _url: Url a la cual se realizara el request
        :type _url: str
        :param _token: Token
        :type _token: str
        :raises BusinessValidationError: En caso de no poder completar el request al servidor
        :return: Objeto Reponse con información de la respuesta del servidor
        :rtype: Response
        """
        self.logger.info('... Realizando GET request al Servidor')

        headers = {}
        if _token:
            headers = {
                'Authorization': f'{_type} {_token}'
            }

        try:
            response = requests.get(_url, headers=headers)

            if response.status_code == 404:
                msg = "... No se encontro recurso en el Servidor ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 401:
                msg = "... No se tienen permisos para consumir este recurso ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 503:
                msg = "... Servidor no disponible ({})".format(
                    response.reason
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code != requests.codes.ok:
                response.encoding = 'utf-8'
                msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                    response.status_code,
                    response.reason,
                    response.json()
                )
                self.logger.error(msg)
                raise ServerError(msg)

            response.encoding = 'utf-8'
            raw_data = response.json()

            msg = "... Respuesta con StatusCode {}".format(response.status_code)
            self.logger.info(msg)

            return raw_data

        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo GET request al Servidor: {msg}")
            raise ServerError(msg)

    def post(self, _url, _data, _token=None, _type="Bearer"):
        self.logger.info('... Realizando POST request al Servidor')

        headers = self._get_Headers(_token, _type)

        try:
            response = requests.post(_url, headers=headers, json=_data)

            if response.status_code == 404:
                msg = "... No se encuentra la url ({}) en el Servidor".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 401:
                msg = "... No se tienen permisos para consumir este recurso ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 503:
                msg = "... Servidor no disponible ({})".format(
                    response.reason
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code != requests.codes.ok:
                response.encoding = 'utf-8'
                msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                    response.status_code,
                    response.reason,
                    response.json()
                )
                self.logger.error(msg)
                raise ServerError(msg)

            response.encoding = 'utf-8'
            raw_data = response.json()

            msg = "... Respuesta con StatusCode {}".format(response.status_code)
            self.logger.info(msg)
            return raw_data

        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo POST request al Servidor: {msg}")
            raise ServerError(msg)

    def post_form(self, _url, _data, _token=None, _type="Bearer"):
        self.logger.info('... Realizando POST request al Servidor')

        headers = {}
        if _token:
            headers = {
                'Authorization': f'{_type} {_token}'
            }

        try:
            response = requests.post(_url, headers=headers, data=_data)

            if response.status_code == 404:
                msg = "... No se encuentra la url ({}) en el Servidor".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 401:
                msg = "... No se tienen permisos para consumir este recurso ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 503:
                msg = "... Servidor no disponible ({})".format(
                    response.reason
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code != requests.codes.ok:
                response.encoding = 'utf-8'
                msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                    response.status_code,
                    response.reason,
                    response.json()
                )
                self.logger.error(msg)
                raise ServerError(msg)

            response.encoding = 'utf-8'
            raw_data = response.json()

            msg = "... Respuesta con StatusCode {}".format(response.status_code)
            self.logger.info(msg)
            return raw_data

        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo POST request al Servidor: {msg}")
            raise ServerError(msg)

    def post_file(self, _url, _file, _token=None, _type="Bearer"):
        self.logger.info('... Realizando POST request al Servidor')

        headers = self._get_Headers(_token, _type)

        try:
            response = requests.post(_url, headers=headers, files=_file)

            if response.status_code == 404:
                msg = "... No se encuentra la url ({}) en el Servidor".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 401:
                msg = "... No se tienen permisos para consumir este recurso ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 503:
                msg = "... Servidor no disponible ({})".format(
                    response.reason
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code != requests.codes.ok:
                response.encoding = 'utf-8'
                msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                    response.status_code,
                    response.reason,
                    response.json()
                )
                self.logger.error(msg)
                raise ServerError(msg)

            response.encoding = 'utf-8'
            raw_data = response.json()

            msg = "... Respuesta con StatusCode {}".format(response.status_code)
            self.logger.info(msg)
            return raw_data

        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo POST request al Servidor: {msg}")
            raise ServerError(msg)

    def get_file(self, _url, _token=None, _type="Bearer"):
        self.logger.info('... Realizando POST request al Servidor')

        headers = {}
        if _token:
            headers = {
                'Authorization': f'{_type} {_token}'
            }

        try:
            response = requests.get(_url, headers=headers)

            if response.status_code == 404:
                msg = "... No se encuentra la url ({}) en el Servidor".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 401:
                msg = "... No se tienen permisos para consumir este recurso ({})".format(
                    _url
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code == 503:
                msg = "... Servidor no disponible ({})".format(
                    response.reason
                )
                self.logger.error(msg)
                raise ServerError(msg)

            if response.status_code != requests.codes.ok:
                response.encoding = 'utf-8'
                msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                    response.status_code,
                    response.reason,
                    response.json()
                )
                self.logger.error(msg)
                raise ServerError(msg)

            response.encoding = 'utf-8'
            return response

        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo GET request al Servidor: {msg}")
            raise ServerError(msg)

    def put(self, _url, _data, _token=None, _type="Bearer"):
        self.logger.info('... Realizando POST request al Servidor')

        headers = self._get_Headers(_token, _type)

        try:
            response = requests.put(_url, headers=headers, data=_data)
        except Exception as e:
            msg = str(e)
            self.logger.error(f"... Fallo POST request al Servidor: {msg}")
            raise ServerError(msg)

        if response.status_code == 404:
            msg = "... No se encuentra la url ({}) en el Servidor".format(
                _url
            )
            self.logger.error(msg)
            raise ServerError(msg)

        if response.status_code == 401:
            msg = "... No se tienen permisos para consumir este recurso ({})".format(
                _url
            )
            self.logger.error(msg)
            raise ServerError(msg)

        if response.status_code == 503:
            msg = "... Servidor no disponible ({})".format(
                response.reason
            )
            self.logger.error(msg)
            raise ServerError(msg)

        if response.status_code != requests.codes.ok:
            response.encoding = 'utf-8'
            msg = "... Respuesta con StatusCode {}: {} -> {}".format(
                response.status_code,
                response.reason,
                response.json()
            )
            self.logger.error(msg)
            raise ServerError(msg)

        response.encoding = 'utf-8'
        raw_data = response.json()

        msg = "... Respuesta con StatusCode {}".format(response.status_code)
        self.logger.info(msg)
        return raw_data

# Python's Libriares
import logging
# import base64

# Django's Libraries
from django.contrib.auth import password_validation
from django.utils import timezone
# from django.core.exceptions import ValidationError
from django.db.models import Q

# Own's Libraries
# from Utils.data import Staker
# from Utils.server import DataBase
# from Utils.errors import NoRecordFoundError
# from Utils.errors import ServerError
from Utils.errors import BusinessError


class Service(object):
    """Clase base para los objectos de la capa de Negocio.
    """

    def __init__(self, _db, _logger=None):
        """Constructor
        """
        self.db = _db
        self.logger = _logger or logging.getLogger(__name__)

    def check_Id(self, _model):
        if _model.id is None:
            raise BusinessError(
                "No se especifico el ID del Registro",
                self.logger
            )

        return True

    def check_Updater(self, _model):
        """Valida que se haya especificado el usuario que actualiza el registro

        :raises NameError: En caso de no se haya especificado
        un usuario actualizador
        :return: Verdadero si las validación paso correctamente
        :rtype: bool
        """
        if _model.updated_by is None:
            raise BusinessError(
                "No se especifico el usuario que actualiza",
                self.logger
            )

        return True

    def check_Creater(self, _model):
        if _model.created_by is None:
            raise BusinessError(
                "No se especifico el usuario que crea el registro",
                self.logger
            )

        return True


class UserService(Service):

    def check_Email(self, _model):
        if _model.email is None:
            raise BusinessError(
                "Favor de proporcionar el email del usuario a actualizar",
                self.logger
            )

        return True

    def check_Position(self, _model):
        if _model.position is None:
            raise BusinessError(
                "No se ha configurado un puesto al usuario. ",
                self.logger
            )

        return True

    def check_AccountStatus(self, _model):
        if _model.is_active is False:
            raise BusinessError(
                "Cuenta de usuario deshabilitada. Favor de "
                "contactar a un administrador del sistema.",
                self.logger
            )

        if _model.is_verified is False:
            raise BusinessError(
                "Cuenta de usuario no verificada. Favor de "
                "contactar a un administrador del sistema.",
                self.logger
            )

        return True

    def set_LoginSuccessData(self, _model):
        _model.success_login_counter += 1
        _model.last_login = timezone.now()
        _model.fail_login_counter = 0

    def set_LoginFailData(self, _model):
        _model.fail_login_counter += 1

        if _model.fail_login_counter >= 4:
            _model.is_active = False
            _model.reset_password = True

    def set_LogoutInformationData(self, _model):
        _model.last_activity = timezone.now()
        _model.session_key = None

    def set_Password(self, _model, _new_password):
        password_validation.validate_password(
            _new_password,
            _model
        )
        _model.reset_password = False
        _model.last_pass_change = timezone.now()
        _model.set_password(_new_password)

    def set_ActivationData(self, _model):
        _model.is_verified = True
        _model.is_active = True
        _model.date_verified = timezone.now()

    def should_UpdatePassword(self, _model, _limit_days):
        if _model.reset_password:
            return True

        if _model.last_pass_change:
            today = timezone.now()
            delta = today - _model.last_pass_change
            # TODO: Change to Global Setting
            if delta.days >= _limit_days:
                return True

        return False

    def get_ById(self, _model):
        self.logger.info(f"--> Buscando Usuario por ID: {_model.id}")
        self.check_Id(_model)

        model = self.db.select_One(_model)
        return model

    def get_ByEmail(self, _model):
        self.logger.info(f"--> Buscando Usuario por Email: {_model.email}")
        self.check_Email(_model)

        model = self.db.select_One(_model)
        return model

    def get_All(self, _model):
        self.logger.info("--> Obteniendo Usuarios")
        exclude = {
            "is_superuser": True
        }
        queryset = self.db.select_Many(_model, _exclude=exclude)
        return queryset

    def update(self, _model):
        self.logger.info(f"--> Actualizar Usuario {_model.id}")
        self.check_Updater(_model)
        self.db.update(_model)
        return True

    def create(self, _model):
        self.logger.info(f"--> Crear Usuario {_model.email}")
        self.check_Creater(_model)

        _model.is_staff = False
        _model.is_superuser = False
        _model.is_verified = False
        _model.first_login = False
        _model.reset_password = False
        _model.is_active = False

        self.db.insert(_model)
        return True


class PositionService(Service):

    def get_ByName(self, _model):
        self.logger.info(f"--> Buscando Puesto por Nombre: {_model.name}")
        if _model.name is None:
            raise BusinessError(
                "Favor de especificar el nombre del Puesto/Rol",
                self.logger
            )

        model = self.db.select_One(_model)
        return model


class PageService(Service):

    def get_Active(self, _model):
        self.logger.info(f"--> Buscar Pagina activa: {_model.key}")
        if _model.key is None:
            raise BusinessError(
                "Favor de especificar la clave de la Pagina",
                self.logger
            )

        model = self.db.select_One(_model)

        if model.is_active is False:
            raise BusinessError(f"Pagina {model.id} desactivada", self.logger)

        return model

    def get_ByKey(self, _model):
        self.logger.info(f"--> Obteniendo Pagina: {_model.key}")

        if _model.key is None:
            raise BusinessError(
                "Favor de especificar la clave de la Pagina",
                self.logger
            )

        model = self.db.select_One(_model)
        return model

    def get_AllMenuOptions(self, _model):
        self.logger.info(
            f"--> Obteniendo las Opciones de Menu: {_model.key}"
        )
        _model.is_menuoption = True

        queryset = self.db.select_Many(_model)
        return queryset


class PageAllowedService(Service):

    def get_MenuOptions(self, _model):
        self.logger.info(
            "--> Buscar Pagina Permitida que son opcion de Menu"
        )
        custom_filters = Q()
        custom_filters.add(Q(page__is_menuoption=True), Q.AND)
        custom_filters.add(Q(position__id=_model.position_id), Q.AND)

        queryset = self.db.select_Many(
            _model, _custom_filters=custom_filters
        )
        return queryset

    def get_Active(self, _model):
        self.logger.info(
            f"--> Buscar Pagina Permitida Activa: {_model.page_id}"
        )

        if _model.page_id is None:
            raise BusinessError(
                "Favor de especificar el id de la Pagina.",
                self.logger
            )

        if _model.position_id is None:
            raise BusinessError(
                "Favor de especificar el id del Permiso.",
                self.logger
            )

        model = self.db.select_One(_model)
        if model.is_active is False:
            raise BusinessError(
                f"Pagina {model.id} desactivada en menu",
                self.logger
            )

        return model


class SmtpService(Service):

    def get_ByName(self, _model):
        self.logger.info(
            f"--> Buscar SMTP Service por Nombre: {_model.name}"
        )

        if _model.name is None:
            raise BusinessError(
                "Favor de especificar el nombre del servicio",
                self.logger
            )

        model = self.db.select_One(_model)
        return model

# Python's Libriares
import logging
import os
import json

# Django's Libraries
from django.db import transaction
from django.db.models import Q
from django.db.models import F
from django.conf import settings

from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.files import File

from django.contrib.auth import password_validation
from django.core.mail.backends.smtp import EmailBackend
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError

from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage

# Third-party Libraries

# Own's Libraries
from Utils.server import DataBase

from Utils.data import EmailSubjectTemplate
from Utils.data import EmailBodyTemplate
from Utils.data import Scribe
from Utils.dto import PageDto
from Utils.dto import ContextItemDto
from Utils.aws import AwsBucket
from Utils.jwt import SecurityJWT
from Utils.errors import SecurityError
from Utils.errors import NoRecordFoundError
from Utils.errors import NoRecordsFoundError
from Utils.errors import DuplicateEntryError
from Utils.server import Connector
from Utils.server import Postman

from core.models import User

from Business.services import UserService


logger = logging.getLogger("app_logger")

EMAIL_NAME = os.getenv('EMAIL_NAME')


class BackofficeWeb(object):
    UserModel = User

    url_landing = 'public:landing'
    url_login = 'backoffice:login'
    url_home = 'backoffice:home'
    url_start = 'backoffice:start'
    url_password_update = 'backoffice:password-update'
    url_password_change_done = 'backoffice:password-change-done'
    url_activation_done = 'backoffice:activation-done'

    @classmethod
    def _get_CurrentPage(self, _request):
        current_page = "{}:{}".format(
            _request.resolver_match.app_name,
            _request.resolver_match.url_name
        )
        return current_page

    @classmethod
    def _get_SystemAccount(self):
        try:
            db = DataBase(_logger=logger)
            user_service = UserService(db, logger)
            model = user_service.get_ById(self.UserModel(id=1))
            return model

        except ValidationError:
            raise NameError("No se ha configurado un Usuario Administrador")

    @classmethod
    def _check_PageAccess(self, _position_model, _page_clave):
        try:
            db = DataBase(_logger=logger)
            page_service = PageService(db, logger)
            page_model = page_service.get_Active(
                self.PageModel(key=_page_clave)
            )

            allowed_service = PageAllowedService(db, logger)
            pageallowed_model = allowed_service.get_Active(
                self.PageAllowedModel(
                    page_id=page_model.id,
                    position_id=_position_model.id
                )
            )
            return pageallowed_model

        except NoRecordFoundError as e:
            if e.model.__class__.__name__ == "Page":
                raise ValidationError(
                    f"No se existe la pagina {_page_clave} en el sistema."
                )

            if e.model.__class__.__name__ == "PageAllowed":
                raise ValidationError(
                    f"El usuario no tiene asignada la pagina {_page_clave}."
                )

    @classmethod
    def _get_Url_ByPermision(self, _user_model):
        url_start = self.url_home
        if _user_model.position.start_page:
            page = _user_model.position.start_page
            url_start = page.key

        return url_start

    @classmethod
    def load_LoginPage(self, _request, _params):
        if _request.user.is_authenticated is False:
            return True

        if _request.user.is_superuser:
            return PageDto(self.url_home)

        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        service.check_Position(_request.user)
        service.check_AccountStatus(_request.user)
        if service.should_UpdatePassword(
            _request.user,
            settings.PASSWORD_LIMIT_DAYS
        ):
            return PageDto(self.url_password_update)

        url = self._get_Url_ByPermision(_request.user)
        return PageDto(url)

    @classmethod
    def login_User(self, _request, _params, _data):
        user_model = authenticate(
            _request,
            username=_data.get('email'),
            password=_data.get('password')
        )

        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        if user_model is None:
            msg = "Cuenta de usuario o contraseña no valida"

            try:
                user_model = service.get_ByEmail(
                    self.UserModel(email=_data.get('email'))
                )
                if user_model.is_superuser:
                    raise ValidationError(msg)

                service.set_LoginFailData(user_model)
                user_model.updated_by = self._get_SystemAccount()
                service.update(user_model)

                if user_model.fail_login_counter >= 4:
                    msg = (
                        "Cuenta de usuario deshabilitada favor "
                        "de consultar al administrador"
                    )

                raise ValidationError(msg)

            except NoRecordFoundError:
                raise ValidationError(msg)

        if user_model.is_superuser is False:
            service.check_Position(user_model)
            service.check_AccountStatus(user_model)

        login(_request, user_model)

        user_model.updated_by = self._get_SystemAccount()
        service.set_LoginSuccessData(user_model)
        service.update(user_model)

        if user_model.is_superuser is True:
            return PageDto(self.url_home)

        if service.should_UpdatePassword(
            user_model,
            settings.PASSWORD_LIMIT_DAYS
        ):
            return PageDto(self.url_password_update)

        url = self._get_Url_ByPermision(_request.user)
        return PageDto(url)

    @classmethod
    def logout_User(self, _request, _params):
        if _request.user.is_authenticated is False:
            return PageDto(self.url_login)

        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        _request.user.updated_by = self._get_SystemAccount()
        service.set_LogoutInformationData(_request.user)
        logout(_request)

        return PageDto(self.url_login)

    @classmethod
    def validate_Security(self, _request, _params):
        if _request.user.is_authenticated is False:
            return PageDto(self.url_landing)

        if _request.user.is_superuser:
            return True

        db = DataBase(_logger=logger)
        user_service = UserService(db, logger)
        user_service.check_AccountStatus(_request.user)
        user_service.check_Position(_request.user)

        if user_service.should_UpdatePassword(
            _request.user,
            settings.PASSWORD_LIMIT_DAYS
        ):
            return PageDto(self.url_password_update)

        self._check_PageAccess(
            _request.user.position,
            self._get_CurrentPage(_request)
        )

    @classmethod
    def load_HomePage(self, _request, _params):
        if _request.user.is_authenticated is False:
            return PageDto(self.url_login)

        if _request.user.is_superuser:
            return True

        db = DataBase(_logger=logger)
        user_service = UserService(db, logger)
        user_service.check_AccountStatus(_request.user)
        user_service.check_Position(_request.user)

        if user_service.should_UpdatePassword(
            _request.user,
            settings.PASSWORD_LIMIT_DAYS
        ):
            return PageDto(self.url_password_update)

        url = self._get_Url_ByPermision(_request.user)
        if url != self._get_CurrentPage(_request):
            return PageDto(url)

    @classmethod
    def get_UserLoggedData(self, _request, _params):
        data = {}
        data['pk'] = ""
        data['email'] = ""
        data['name'] = ""
        data['is_superuser'] = ""
        data['position_name'] = ""
        data['first_login'] = "no"
        data['last_campaign_rol'] = ""
        data['menu'] = []

        user = _request.user

        if user.is_anonymous:
            return data

        if user.first_login:
            data['first_login'] = "no"

        data['pk'] = user.pk
        data['email'] = user.email
        if data['last_campaign_rol']:
            user.last_campaign_rol = data['last_campaign_rol']

        if user.name:
            data['name'] = user.name
        else:
            data['name'] = user.email

        data['is_superuser'] = user.is_superuser

        db = DataBase(_logger=logger)
        if user.is_superuser:
            data['position_name'] = "ADMINISTRADOR"
            try:
                service_page = PageService(db, logger)
                data['menu'] = service_page.get_AllMenuOptions(
                    self.PageModel()
                )

            except NoRecordsFoundError:
                logger.error("No se existen opciones configuradas")
                pass

        elif user.position:
            data['position_name'] = user.position.name

            try:
                service_page = PageAllowedService(db, logger)
                options = service_page.get_MenuOptions(
                    self.PageAllowedModel(position_id=user.position_id)
                )
                for option in options:
                    data['menu'].append(option.page)

            except NoRecordsFoundError:
                logger.error("No se existen opciones configuradas")
                pass

        print(data)
        return data

    @classmethod
    def load_PasswordUpdatePage(self, _request, _params):
        if _request.user.is_authenticated is False:
            return PageDto(self.url_login)

        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        service.check_AccountStatus(_request.user)
        service.check_Position(_request.user)

        if service.should_UpdatePassword(
            _request.user,
            settings.PASSWORD_LIMIT_DAYS
        ) is False:
            url = self._get_Url_ByPermision(_request.user)
            return PageDto(url)

    @classmethod
    def send_PasswordChangeEmail(self, _request, _params, _data):
        db = DataBase(_logger=logger)
        user_service = UserService(db, logger)
        user_model = user_service.get_ByEmail(
            self.UserModel(email=_data.get('email'))
        )

        if user_model.is_superuser is False:
            user_service.check_AccountStatus(user_model)

        subject_template = EmailSubjectTemplate(
            'email/backoffice_email_change_subject.txt',
            {'app': settings.APP_NAME}
        )

        current_site = get_current_site(_request)
        body_template = EmailBodyTemplate(
            'email/backoffice_email_change_body.html',
            {
                'app': settings.APP_NAME,
                'email': user_model.email,
                'domain': current_site.domain,
                'site_name': current_site.name,
                'uid': urlsafe_base64_encode(force_bytes(user_model.id)),
                'token': default_token_generator.make_token(user_model),
                'protocol': _request.scheme,
            }
        )

        to = [user_model.email, ]

        smtp_service = SmtpService(db, logger)
        smtp_model = smtp_service.get_ByName(
            self.ThirdPartyServiceModel(name="EMAIL_TEST")
        )

        email_backend = EmailBackend(
            host=smtp_model.host,
            port=smtp_model.port,
            username=smtp_model.username,
            password=smtp_model.password,
            use_tls=smtp_model.use_tls,
            fail_silently=smtp_model.fail_silently
        )

        postman = Postman(email_backend)
        postman.send_Email(
            smtp_model.username,
            to,
            subject_template.render(),
            body_template.render()
        )

        messages.success(
            _request,
            "Se envió un email con instrucciones "
            "para establecer una nueva contraseña."
        )

    @classmethod
    def update_Password(self, _request, _params, _data):
        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        model = service.get_ByEmail(
            self.UserModel(email=_data.get('email'))
        )

        url = None
        if 'param1' in _params:
            if _params['param1'] == 'user':
                model.updated_by = _request.user
        else:
            model.updated_by = self._get_SystemAccount()
            url = PageDto(self.url_home)

        service.set_Password(model, _data.get('password1'))
        service.update(model)
        update_session_auth_hash(_request, model)

        if url:
            return url

    @classmethod
    def load_UserListPage(self, _request, _params):
        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        queryset = service.get_All(self.UserModel())
        context_item = ContextItemDto('records', queryset)

        return context_item

    @classmethod
    def _send_EmailAdminActivation(self, _request, _user_model):
        subject_template = EmailSubjectTemplate(
            'email/backoffice_email_activation_subject.txt',
            {'app': settings.APP_NAME}
        )
        current_site = get_current_site(_request)
        body_template = EmailBodyTemplate(
            'email/backoffice_email_admin_activation_body.html',
            {
                'app': settings.APP_NAME,
                'email': _user_model.email,
                'evaluator_name': _user_model.name,
                'domain': current_site.domain,
                'site_name': current_site.name,
                'uid': urlsafe_base64_encode(force_bytes(_user_model.id)),
                'token': default_token_generator.make_token(_user_model),
                'protocol': _request.scheme,
            }
        )

        db = DataBase(_logger=logger)
        smtp_service = SmtpService(db, logger)
        smtp_model = smtp_service.get_ByName(
            self.ThirdPartyServiceModel(name=EMAIL_NAME)
        )

        email_backend = EmailBackend(
            host=smtp_model.host,
            port=smtp_model.port,
            username=smtp_model.username,
            password=smtp_model.password,
            use_tls=smtp_model.use_tls,
            fail_silently=smtp_model.fail_silently
        )

        postman = Postman(email_backend)
        postman.send_Email(
            smtp_model.username,
            [_user_model.email, ],
            subject_template.render(),
            body_template.render()
        )

    @classmethod
    def get_User(self, _request, _params):
        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        model = service.get_ById(self.UserModel(id=_params['param1']))

        if hasattr(model, "profile"):
            model.description = model.profile.description
            model.facebook = model.profile.facebook
            model.instagram = model.profile.instagram
            model.twitter = model.profile.twitter

        return model

    @classmethod
    def post_UserNewPage(self, _request, _params, _data):
        with transaction.atomic():
            db = DataBase(_logger=logger)
            model_user = self._create_User(_request, _data)

            # Get Position
            service_position = PositionService(db, logger)
            model_position = service_position.get_ByName(
                self.PositionModel(name="ADMINISTRADOR")
            )

            model_user.position = model_position
            model_user.updated_by = _request.user

            service_user = UserService(db, logger)
            service_user.update(model_user)

            service_profile = ProfileService(db, logger)
            model_profile = self.ProfileModel()
            Scribe.fill_DictWithOther(model_profile, _data)
            model_profile.user = model_user
            model_profile.created_by = _request.user

            if _request.FILES:
                image = _request.FILES['photo']
                model_profile.photo = File(image)

            service_profile.create(model_profile)
            # service_profile.update(model_profile)

            self._send_EmailAdminActivation(_request, model_user)

            messages.success(
                _request,
                "Usuario creado con exito. Se envió un email con instrucciones "
                "para activar la cuenta."
            )

            return PageDto(self.url_users)

    @classmethod
    def send_ActivationUser(self, _request, _params):
        db = DataBase(_logger=logger)
        service = UserService(db, logger)
        model = service.get_ById(self.UserModel(id=_params['param1']))

        self._send_EmailAdminActivation(_request, model)
        return True

    @classmethod
    def get_UserEditPage(self, _request, _params):
        context_item = ContextItemDto('user_id', _params['param1'])
        return context_item

    @classmethod
    def post_UserEditPage(self, _request, _params, _data):
        with transaction.atomic():
            db = DataBase(_logger=logger)
            service_user = UserService(db, logger)
            model_user = service_user.get_ById(self.UserModel(pk=_params['param1']))

            Scribe.fill_DictWithOther(model_user, _data)
            model_user.updated_by = _request.user
            service_user.update(model_user)

            service_profile = ProfileService(db, logger)

            if hasattr(model_user, "profile"):
                model_profile = model_user.profile
                if _data['photo'] is None:
                    del _data['photo']

                Scribe.fill_DictWithOther(model_profile, _data)
                model_user.profile.updated_by = _request.user
                service_profile.update(model_profile)

            else:
                model_profile = self.ProfileModel()
                if _data['photo'] is None:
                    del _data['photo']

                Scribe.fill_DictWithOther(model_profile, _data)
                model_profile.user = model_user
                model_profile.created_by = _request.user
                service_profile.create(model_profile)

            messages.success(
                _request,
                f"Usuario {model_user.email} actualizado correctamente"
            )
            return PageDto(self.url_users)

    @classmethod
    def get_Users(self, _request, _params):
        try:
            db = DataBase(_logger=logger)
            service = UserService(db, logger)
            queryset = service.get_All(self.UserModel())
            return queryset

        except NoRecordsFoundError:
            return []

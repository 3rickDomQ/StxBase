# Django's Libraries
from django.contrib.auth.views import PasswordResetConfirmView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
# from django.utils.http import urlsafe_base64_decode
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters


# Own's Libriries
from Utils.views import SimpleView
from Utils.views import FormView
from Utils.views import SecurityView
from Utils.views import SecurityFormView

from Business.controllers import BackofficeWeb

from .forms import LoginForm
from .forms import EmailForm
from .forms import PasswordSaveForm
from .forms import PasswordChangeConfirmForm
from .forms import UserForm
from .forms import UserNewForm
from .forms import CampaignForm
from .forms import PollForm
from .forms import ActivationConfirmForm
from .forms import CiudadanoActivationConfirmForm

UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class LoginView(FormView):
    page_title = "Login"
    template_name = "pages/backoffice_login.html"
    form_class = LoginForm
    app_class = BackofficeWeb
    get_method = "load_LoginPage"
    post_method = "login_User"


class LogoutView(SimpleView):
    page_title = "Logout"
    app_class = BackofficeWeb
    get_method = "logout_User"


class HomeView(SimpleView):
    page_title = "Dashboard"
    template_name = "pages/backoffice_home.html"
    app_class = BackofficeWeb
    get_method = "load_HomePage"


class PasswordUpdateView(FormView):
    page_title = "Actualización de contraseña"
    template_name = "pages/backoffice_pass_update.html"
    form_class = PasswordSaveForm
    app_class = BackofficeWeb
    get_method = "load_PasswordUpdatePage"
    post_method = "update_Password"
    initial_data_method = "get_UserLoggedData"


class PasswordChangeRequestView(FormView):
    page_title = "Cambio de Contraseña"
    template_name = "pages/backoffice_pass_change_request.html"
    form_class = EmailForm
    app_class = BackofficeWeb
    post_method = "send_PasswordChangeEmail"


class PasswordChangeConfirmView(PasswordResetConfirmView):
    form_class = PasswordChangeConfirmForm
    template_name = 'pages/backoffice_pass_change_confirm.html'
    success_url = reverse_lazy(BackofficeWeb.url_password_change_done)

    def form_valid(self, form):
        # user = form.save()
        data = form.cleaned_data
        data['email'] = self.user.email

        BackofficeWeb.update_Password(
            self.request,
            {"param1": 'system'},
            data
        )

        # del self.request.session['_password_reset_token']
        # if self.post_reset_login:
        #     auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)


class PasswordChangeDoneView(SimpleView):
    page_title = "Cambio de Contraseña exitosa"
    template_name = 'pages/backoffice_pass_change_done.html'


class CandidateActivationConfirmView(PasswordResetConfirmView):
    form_class = CiudadanoActivationConfirmForm
    template_name = "pages/backoffice_ciudadano_activation_confirm.html"
    success_url = reverse_lazy(BackofficeWeb.url_activation_done)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            # if self.user.is_verified and self.user.is_active:
            #     return HttpResponseRedirect(self.get_success_url())

            token = kwargs['token']
            if token == INTERNAL_RESET_URL_TOKEN:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        data = form.cleaned_data
        data['email'] = self.user.email
        data['campaign'] = int(self.request.path.split('/')[-2])

        BackofficeWeb.activate_Candidate(
            self.request,
            {"param1": 'system'},
            data
        )
        return HttpResponseRedirect(self.get_success_url())


class OrganizationActivationConfirmView(PasswordResetConfirmView):
    form_class = CiudadanoActivationConfirmForm
    template_name = "pages/backoffice_ciudadano_activation_confirm.html"
    success_url = reverse_lazy(BackofficeWeb.url_activation_done)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            # if self.user.is_verified and self.user.is_active:
            #     return HttpResponseRedirect(self.get_success_url())

            token = kwargs['token']
            if token == INTERNAL_RESET_URL_TOKEN:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        data = form.cleaned_data
        data['email'] = self.user.email
        data['campaign'] = int(self.request.path.split('/')[-2])

        BackofficeWeb.activate_Organization(
            self.request,
            {"param1": 'system'},
            data
        )
        return HttpResponseRedirect(self.get_success_url())


class CollaboratorActivationConfirmView(PasswordResetConfirmView):
    form_class = CiudadanoActivationConfirmForm
    template_name = "pages/backoffice_ciudadano_activation_confirm.html"
    success_url = reverse_lazy(BackofficeWeb.url_activation_done)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            # if self.user.is_verified and self.user.is_active:
            #     return HttpResponseRedirect(self.get_success_url())

            token = kwargs['token']
            if token == INTERNAL_RESET_URL_TOKEN:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        data = form.cleaned_data
        data['email'] = self.user.email
        data['campaign'] = int(self.request.path.split('/')[-2])

        BackofficeWeb.activate_Collaborator(
            self.request,
            {"param1": 'system'},
            data
        )
        return HttpResponseRedirect(self.get_success_url())


class EvaluatorActivationConfirmView(PasswordResetConfirmView):
    form_class = CiudadanoActivationConfirmForm
    template_name = "pages/backoffice_ciudadano_activation_confirm.html"
    success_url = reverse_lazy(BackofficeWeb.url_activation_done)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            # if self.user.is_verified and self.user.is_active:
            #     return HttpResponseRedirect(self.get_success_url())

            token = kwargs['token']
            if token == INTERNAL_RESET_URL_TOKEN:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        data = form.cleaned_data
        data['email'] = self.user.email
        data['campaign'] = int(self.request.path.split('/')[-2])

        BackofficeWeb.activate_Evaluator(
            self.request,
            {"param1": 'system'},
            data
        )
        return HttpResponseRedirect(self.get_success_url())


class AdminActivationConfirmView(PasswordResetConfirmView):
    form_class = ActivationConfirmForm
    template_name = "pages/backoffice_admin_activation_confirm.html"
    success_url = reverse_lazy(BackofficeWeb.url_activation_done)

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            # if self.user.is_verified and self.user.is_active:
            #     return HttpResponseRedirect(self.get_success_url())

            token = kwargs['token']
            if token == INTERNAL_RESET_URL_TOKEN:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, INTERNAL_RESET_URL_TOKEN)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        data = form.cleaned_data
        data['email'] = self.user.email

        BackofficeWeb.activate_Admin(
            self.request,
            data
        )
        return HttpResponseRedirect(self.get_success_url())


class ActivationDoneView(SimpleView):
    page_title = "Activacion de cuenta exitosa"
    template_name = 'pages/backoffice_activation_done.html'


class UserListView(SecurityView):
    page_title = "Listado de Usuarios"
    template_name = "pages/backoffice_user_list.html"
    module_key = "USERS"
    app_class = BackofficeWeb
    security_method = "validate_Security"
    get_method = "load_UserListPage"
    toolbar = [
        {
            'label': 'Nuevo',
            'url': reverse_lazy(
                'backoffice:user-new'
            ),
            'icon': 'fas fa-plus-circle'
        }
    ]


class UserNewView(SecurityFormView):
    page_title = "Creación de Usuario"
    template_name = "pages/backoffice_user_new.html"
    form_class = UserNewForm
    module_key = "USERS"
    app_class = BackofficeWeb
    security_method = "validate_Security"
    post_method = "post_UserNewPage"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:user-list')
        },
        {
            'label': 'Nuevo',
            'url': '#'
        }
    ]


class UserEditView(SecurityFormView):
    page_title = "Edición del Usuario"
    template_name = "pages/backoffice_user_edit.html"
    form_class = UserForm
    module_key = "USERS"
    app_class = BackofficeWeb
    get_method = "get_UserEditPage"
    instance_method = "get_User"
    initial_data_method = "get_UserData"
    security_method = "validate_Security"
    post_method = "post_UserEditPage"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:user-list')
        },
        {
            'label': 'Edición',
            'url': '#'
        }
    ]


class ProfileFilesView(SecurityView):
    page_title = "Edición del Usuario"
    template_name = "pages/backoffice_user_files.html"
    module_key = "USERS"
    security_method = "validate_Security"
    app_class = BackofficeWeb
    get_method = "load_ProfileFilesPage"


class CampaignListView(SecurityView):
    page_title = "Administración de Candidaturas"
    template_name = "pages/backoffice_campaign_list.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    security_method = "validate_Security"
    get_method = "load_CampaignListPage"
    toolbar = [
        {
            'label': 'Nueva',
            'url': reverse_lazy("backoffice:campaign-new"),
            'icon': 'fas fa-plus-circle'
        }
    ]


class CampaignNewView(SecurityFormView):
    page_title = "Creación de Candidatura"
    template_name = "pages/backoffice_campaign_new.html"
    form_class = CampaignForm
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    security_method = "validate_Security"
    post_method = "create_Campaign"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:campaign-list')
        },
        {
            'label': 'Nuevo',
            'url': '#'
        }
    ]


class CampaignEditView(SecurityFormView):
    page_title = "Edición del Candidatura"
    template_name = "pages/backoffice_campaign_edit.html"
    form_class = CampaignForm
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignEditPage"
    instance_method = "get_Campaign"
    security_method = "validate_Security"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:campaign-list')
        },
        {
            'label': 'Edición',
            'url': '#'
        }
    ]


class CampaignFilesView(SecurityView):
    page_title = "Edición del Candidatura"
    template_name = "pages/backoffice_campaign_files.html"
    module_key = "CAMPAIGNS"
    security_method = "validate_Security"
    app_class = BackofficeWeb
    get_method = "load_CampaignFilesPage"


class CampaignReviewView(SecurityView):
    page_title = "Edición del Candidatura"
    template_name = "pages/backoffice_campaign_review.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignEditPage"
    security_method = "validate_Security"


class CampaignCandidateView(SecurityView):
    page_title = "Candidatura - Candidato"
    template_name = "pages/backoffice_campaign_candidate.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignCandidatePage"
    security_method = "validate_Security"


class CampaignEvaluadorView(SecurityView):
    page_title = "Candidatura Evaluador"
    template_name = "pages/backoffice_campaign_evaluator.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignEvaluatorPage"
    security_method = "validate_Security"


class CampaignExamView(SecurityView):
    page_title = "Examen"
    template_name = "pages/backoffice_campaign_exam.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignExamPage"
    security_method = "validate_Security"


class CampaignEvaluarView(SecurityView):
    page_title = "Evaluar"
    template_name = "pages/backoffice_campaign_evaluar.html"
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_CampaignEvaluarPage"
    security_method = "validate_Security"


class CampaignPollNewView(SecurityFormView):
    page_title = "Crear Encuesta"
    template_name = "pages/backoffice_poll_new.html"
    form_class = PollForm
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    # get_method = "load_CampaignEditPage"
    security_method = "validate_Security"
    post_method = "create_Poll"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:campaign-list')
        },
        {
            'label': 'Candidatura',
            'url': '#'
        },
        {
            'label': 'Encuesta',
            'url': '#'
        }
    ]


class CampaignPollEditView(SecurityFormView):
    page_title = "Edición de Encuesta"
    template_name = "pages/backoffice_poll_edit.html"
    form_class = PollForm
    module_key = "CAMPAIGNS"
    app_class = BackofficeWeb
    get_method = "load_PollEditPage"
    instance_method = "get_Poll"
    security_method = "validate_Security"
    breadcrumb = [
        {
            'label': 'Listado',
            'url': reverse_lazy('backoffice:campaign-list')
        },
        {
            'label': 'Candidatura',
            'url': '#'
        },
        {
            'label': 'Encuesta',
            'url': '#'
        }
    ]


class CampaignAvatarView(SimpleView):
    page_title = "Calificación por Avatar"
    template_name = "pages/backoffice_avatar.html"
    app_class = BackofficeWeb
    get_method = "load_AvatarPage"


class AvatarProductView(SimpleView):
    page_title = "Administración de Entrevistas de Avatar"
    template_name = "pages/backoffice_avatar_admin.html"
    app_class = BackofficeWeb
    # get_method = "load_AvatarAdminPage"


class TestingView(SimpleView):
    page_title = "Testing"
    template_name = "pages/backoffice_testing.html"
    app_class = BackofficeWeb
    get_method = "load_AvatarPage"

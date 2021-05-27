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


UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


# class LoginView(FormView):
#     page_title = "Login"
#     template_name = "pages/backoffice_login.html"
#     form_class = LoginForm
#     app_class = BackofficeWeb
#     get_method = "load_LoginPage"
#     post_method = "login_User"

# Django's Libraries
from django import forms
# from django.utils.safestring import mark_safe
# from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import password_validation
from django.forms import ModelForm
from django.forms import Form
# from django.forms import Select
# from django.forms import DateField
# from django.forms import DateInput
from django.forms import CharField
# from django.forms import ChoiceField
from django.forms import ModelChoiceField
from django.forms import EmailField
from django.forms import TextInput
from django.forms import Textarea
from django.forms import URLField
from django.forms import FileField
from django.forms import EmailInput
from django.forms import PasswordInput

# from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Own's Libraries
from Business.controllers import BackofficeWeb


class LoginForm(Form):
    email = EmailField(
        widget=TextInput(attrs={
            'placeholder': 'Correo Electrónico'
        })
    )
    password = CharField(
        widget=PasswordInput(attrs={
            'placeholder': 'Contraseña'
        })
    )


class EmailForm(Form):
    email = CharField(
        label='',
        widget=EmailInput()
    )


class PasswordChangeConfirmForm(AdminPasswordChangeForm):
    # help_text=password_validation.password_validators_help_text_html(),
    password1 = CharField(
        label='Nueva contraseña',
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        help_text=(
            "Para verificar, introduzca la misma "
            "contraseña que introdujo antes."
        ),
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


class ActivationConfirmForm(AdminPasswordChangeForm):
    password1 = CharField(
        label='Nueva contraseña',
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        help_text=(
            "Para verificar, introduzca la misma "
            "contraseña que introdujo antes."
        ),
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


class CiudadanoActivationConfirmForm(AdminPasswordChangeForm):
    description = CharField(
        label='Descripción',
        widget=TextInput(
            attrs={'class': 'form-control'}
        ),
        help_text="Descripción de profesión o breve descripción de su organización"
    )
    facebook = CharField(
        label='Facebook',
        required=False,
        widget=TextInput(
            attrs={'class': 'form-control'}
        )
    )
    instagram = CharField(
        label='Instragram',
        required=False,
        widget=TextInput(
            attrs={'class': 'form-control'}
        )
    )
    twitter = CharField(
        label='twitter',
        required=False,
        widget=TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = CharField(
        label='Nueva contraseña',
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        help_text=(
            "Para verificar, introduzca la misma "
            "contraseña que introdujo antes."
        ),
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


class PasswordSaveForm(Form):
    error_messages = {
        'password_mismatch': _(
            "Las contraseñas no coinciden."
        ),
    }

    email = CharField()
    password1 = CharField(
        label='Nueva contraseña',
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        widget=PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = CharField(
        label='Confirmar contraseña',
        help_text=(
            "Para verificar, introduzca la misma "
            "contraseña que introdujo antes."
        ),
        strip=False,
        widget=PasswordInput(
            attrs={'class': 'form-control', 'autofocus': True}
        )
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2


class UserForm(ModelForm):
    description = CharField(
        required=False,
        widget=Textarea(attrs={"rows": 5, "cols": 20})
    )
    facebook = CharField(required=False)
    instagram = CharField(required=False)
    twitter = CharField(required=False)
    photo = FileField(required=False)

    class Meta:
        model = BackofficeWeb.UserModel
        fields = [
            "name",
            "email",
            "position",
            "is_active"
        ]


class UserNewForm(ModelForm):
    description = CharField(
        required=False,
        widget=Textarea(attrs={"rows": 5, "cols": 20})
    )
    facebook = CharField(required=False)
    instagram = CharField(required=False)
    twitter = CharField(required=False)
    photo = FileField(required=False)

    def __init__(self, *args, **kwargs):
        super(UserNewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BackofficeWeb.UserModel
        fields = [
            "name",
            "email",
        ]
        exclude = [
            "position",
            "is_active"
        ]

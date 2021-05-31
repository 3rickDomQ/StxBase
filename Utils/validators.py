# Python's Libraries
import re
from datetime import datetime

# Django's Libraries
from django.utils.timezone import make_aware
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

#Own Libraries
from custom_choices import DateRangeType


@deconstructible
class BaseValidator:
    message = _('Ensure this value is %(limit_value)s (it is %(show_value)s).')
    code = 'limit_value'

    def __init__(self, limit_value, message=None):
        self.limit_value = limit_value
        if message:
            self.message = message

    def __call__(self, value):
        cleaned = self.clean(value)
        params = {
            'limit_value': self.limit_value,
            'show_value': cleaned,
            'value': value
        }
        if self.compare(cleaned, self.limit_value):
            raise ValidationError(self.message, code=self.code, params=params)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.limit_value == other.limit_value and
            self.message == other.message and
            self.code == other.code
        )

    def compare(self, a, b):
        return a is not b

    def clean(self, x):
        return x


@deconstructible
class MinValueValidator(BaseValidator):
    message = _(
        'Ensure this value is greater '
        'than or equal to %(limit_value)s.'
    )
    code = 'min_value'

    def compare(self, a, b):
        return a < b


class HasUpperCaseValidator:

    def validate(self, password, user=None):
        upper_qty = 0
        for letter in password:
            if letter.isupper():
                upper_qty += 1

        if upper_qty == 0:
            raise ValidationError(
                'La contraseña debe contener al menos un '
                'caracter en mayúscula.',
                code='password_without_upper',
            )

    def get_help_text(self):
        return "La contraseña debe contener al menos un caracter en mayúscula."


class HasNumberValidator:

    def validate(self, password, user=None):
        number_qty = 0

        for letter in password:
            if letter.isdigit():
                number_qty += 1

        if number_qty == 0:
            raise ValidationError(
                "La contraseña debe contener al menos un número.",
                code='password_without_number',
            )

    def get_help_text(self):
        return "La contraseña debe contener al menos un número."


class HasSpecialCharacterValidator:

    def validate(self, password, user=None):
        special_str = re.compile(
            '[@_!#$%^&*()<>?|}{~:]'
        )

        if(special_str.search(password) is None):
            raise ValidationError(
                "La contraseña debe contener al menos un caracter "
                "especial ([@_!#$%^&*()<>?|}{~:])",
                code='password_without_special',
            )

    def get_help_text(self):
        text = (
            "La contraseña debe contener al menos un caracter "
            "especial ([@_!#$%^&*()<>?|}{~:])."
        )
        return text


def validate_DontHaveWhitespaces(value):
    if ' ' in value:
        raise ValidationError(
            "No puede contener espacios en blanco.",
            code='with_whitespaces',
        )


class Chronos(object):

    @classmethod
    def validate_DateRange(self, _init_date, _end_date):
        if _init_date and _end_date:
            if _init_date < _end_date is False:
                raise ValidationError("Las fechas son incorrectas")

        else:
            raise ValidationError(
                "Se deben proporcionar InitDate and EndDate"
            )

        return True

    @classmethod
    def convert_ToAware(self, _str_datetime):
        try:
            aware_date = make_aware(datetime.strptime(_str_datetime, "%Y-%m-%dT%H:%M:%S"))

        except Exception:
            raise ValidationError(
                "Fallo conversión de fechas"
            )

        return aware_date

    @classmethod
    def convert_ToStrDateTime(self, _str_date, _choice: DateRangeType):
        # Use to convert only date formated string to datetime format
        # _choice must be a DateRangeType attribute
        try:
            if _choice.value == DateRangeType.Start.value:
                datetime = _str_date + "T00:00:00"
            elif _choice.value == DateRangeType.End.value:
                datetime = _str_date + "T23:59:59"
            else:
                raise ValidationError(
                    "el valor del argumento _choice"
                    "debe ser 'Start' ó 'End'"
                )
        except Exception:
            raise ValidationError(
                "Fallo conversión de fechas"
            )

        return datetime

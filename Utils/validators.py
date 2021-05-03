# Python's Libraries
import re

# Django's Libraries
from django.core.exceptions import ValidationError


class HasUpperCaseValidator:

    def validate(self, password, user=None):
        upper_qty = 0
        for l in password:
            if l.isupper():
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

        for l in password:
            if l.isdigit():
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


class ModelValidator:

    @classmethod
    def check_DontHaveWhitespaces(self, value):
        if ' ' in value:
            raise ValidationError(
                "No puede contener espacios en blanco.",
                code='with_whitespaces',
            )

# Django's Libraries
from django.core.exceptions import ValidationError as DValidation
from django.core.exceptions import FieldError

# Third-party Libraries
from rest_framework.exceptions import ValidationError as RValidation
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from Utils.errors import BusinessError


def base_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # check that a ValidationError exception is raised
    if isinstance(exc, NameError):
        return Response(
            {'detail': str(str(exc))},
            status=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, BusinessError):
        return Response(
            {'detail': exc.message},
            status=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, DValidation):
        return Response(
            {'detail': exc.message},
            status=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, FieldError):
        return Response(
            {'detail': str(str(exc))},
            status=status.HTTP_400_BAD_REQUEST
        )
        # # here prepare the 'custom_error_response' and
        # # set the custom response data on response object
        # if response.data.get("username", None):
        #     response.data = response.data["username"][0]
        # elif response.data.get("email", None):
        #     response.data = response.data["email"][0]
        # elif response.data.get("password", None):
        #     response.data = response.data["password"][0]

    return response

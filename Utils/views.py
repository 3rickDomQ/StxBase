# Django's Libraries
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404

from django.core.exceptions import ValidationError
# from abc import ABC
# from abc import abstractmethod

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View
from django.db.models.query import QuerySet


# Own's Libraries
from .dto import PageDto
from .dto import ContextItemDto


class SimpleView(View):
    page_title = None
    context = {}
    breadcrumb = []
    toolbar = []
    request = None
    param = None
    custom_param = None
    module_key = None
    app_class = None
    get_method = None
    post_method = None

    def get_PageName(self):
        """Configura el nombre de la pagina (nombre que aparece en la
        pestaña del navegador) y lo agrega a la atributo :param:`context`

        :raises ImproperlyConfigured: Cuando no se ha inicializado el
        atributo :func:`page_title`
        """

        if self.page_title is None:
            raise ImproperlyConfigured(
                "Favor de especificar el nombre de plagina con page_title"
            )

        value = "{} - {}".format(
            self.page_title,
            settings.APP_NAME
        )
        return value

    def get_PageTitle(self):
        """Configura el título de la página.

        :raises ImproperlyConfigured: Cuando no se ha inicializado el
        atributo :func:`page_title`
        """

        if self.page_title is None:
            raise ImproperlyConfigured(
                "Favor de especificar el nombre de la página con page_title"
            )

        value = self.page_title
        return value

    def set_ErrorMessages(self, _error):
        """Configura los mensajes de error que aparecerá en la vista.

        :param _error: "Texto o lista con textos que se mostraran en la vista
        :type _error: str or list
        """
        if isinstance(_error, ValidationError):
            if len(_error.error_list) > 1:
                for item in _error.error_list:
                    messages.error(self.request, item.message)
            else:
                messages.error(self.request, _error.messages[0])
        else:
            messages.error(self.request, str(_error))

    def get_Breadcrumb(self):
        if self.breadcrumb:
            return self.breadcrumb

    def get_Toolbar(self):
        if self.toolbar:
            return self.toolbar

    def call_GetBsnMethod(self):
        if self.get_method:
            if self.app_class is None:
                raise ImproperlyConfigured(
                    "Favor de especificar una app_class"
                )

            try:
                return getattr(self.app_class, self.get_method)(
                    self.request,
                    self.params
                )

            except Exception as error:
                self.set_ErrorMessages(error)
                context_item = ContextItemDto('error', error)
                return context_item

    def call_PostBsnMethod(self):
        if self.post_method:
            if self.app_class is None:
                raise ImproperlyConfigured(
                    "Favor de especificar una app_class"
                )

            try:
                return getattr(self.app_class, self.post_method)(
                    self.request,
                    self.params
                )

            except Exception as error:
                self.set_ErrorMessages(error)
                context_item = ContextItemDto('error', error)
                return context_item

    def set_Params(self, _params):
        self.params = _params

    # def set_Params(self, _param1, _param2):
    #     self.params = []
    #     if _param1:
    #         self.params.append(_param1)

    #     if _param2:
    #         self.params.append(_param2)

    def get_CustomParams(self):
        if self.custom_param:
            return self.custom_param

    def get_ModuleKey(self):
        if self.module_key:
            return self.module_key

    def get(self, request, *args, **kwargs):
        context = {}
        self.request = request
        context["page_name"] = self.get_PageName()
        context["page_title"] = self.get_PageTitle()
        context["breadcrumb"] = self.get_Breadcrumb()
        context["toolbar"] = self.get_Toolbar()
        context['custom_param'] = self.get_CustomParams()
        context["module_key"] = self.get_ModuleKey()

        # self.set_Params(param1, param2)
        self.set_Params(kwargs)

        response = self.call_GetBsnMethod()
        if isinstance(response, QuerySet):
            context['records'] = response

        if isinstance(response, PageDto):
            return redirect(response.get_Url())

        if isinstance(response, ContextItemDto):
            context[response.key] = response.value

        for key, value in self.context.items():
            context[key] = value

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        self.request = request
        context["page_name"] = self.get_PageName()
        context["page_title"] = self.get_PageTitle()
        context["breadcrumb"] = self.get_Breadcrumb()
        context["toolbar"] = self.get_Toolbar()
        context['custom_param'] = self.get_CustomParams()
        context["module_key"] = self.get_ModuleKey()

        # self.set_Params(param1, param2)
        self.set_Params(kwargs)

        response = self.call_PostBsnMethod()
        if isinstance(response, QuerySet):
            context['records'] = response

        if isinstance(response, PageDto):
            return redirect(response.get_Url())

        if isinstance(response, ContextItemDto):
            context[response.key] = response.value

        for key, value in self.context.items():
            context[key] = value

        return render(request, self.template_name, context)


class FormView(SimpleView):
    form_class = None
    data = None
    instance = None
    initial_data = None
    instance_method = None
    initial_data_method = None

    def init_Form(self):
        if self.form_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar clase de formulario"
            )

        if self.request.POST:
            if self.instance:
                form = self.form_class(
                    self.request.POST,
                    self.request.FILES,
                    instance=self.instance,
                )
            else:
                form = self.form_class(self.request.POST, self.request.FILES)

        elif self.instance:
            if self.initial_data:
                form = self.form_class(
                    instance=self.instance,
                    initial=self.initial_data
                )
            else:
                form = self.form_class(instance=self.instance)

        else:
            if self.initial_data:
                form = self.form_class(initial=self.initial_data)
            else:
                form = self.form_class()

        self.context['form'] = form
        return form

    def call_GetInstanceMethod(self):
        if self.instance_method:
            if self.app_class is None:
                raise ImproperlyConfigured(
                    "Favor de especificar una app_class"
                )

            try:
                return getattr(self.app_class, self.instance_method)(
                    self.request,
                    self.params
                )
            except Exception as error:
                self.set_ErrorMessages(error)

    def call_GetInitialDataMethod(self):
        if self.initial_data_method:
            if self.app_class is None:
                raise ImproperlyConfigured(
                    "Favor de especificar una app_class"
                )

            try:
                return getattr(self.app_class, self.initial_data_method)(
                    self.request,
                    self.params
                )
            except Exception as error:
                self.set_ErrorMessages(error)

    def call_PostBsnMethod(self):
        if self.post_method:
            if self.app_class is None:
                raise ImproperlyConfigured(
                    "Favor de especificar una app_class"
                )

            try:
                return getattr(self.app_class, self.post_method)(
                    self.request,
                    self.params,
                    self.data
                )
            except Exception as error:
                self.set_ErrorMessages(error)
                context_item = ContextItemDto('error', error)
                return context_item

    def get(self, request, *args, **kwargs):
        context = {}
        self.request = request

        context["page_name"] = self.get_PageName()
        context["page_title"] = self.get_PageTitle()
        context["breadcrumb"] = self.get_Breadcrumb()
        context["toolbar"] = self.get_Toolbar()
        context['custom_param'] = self.get_CustomParams()
        context["module_key"] = self.get_ModuleKey()

        # self.set_Params(param1, param2)
        self.set_Params(kwargs)

        self.instance = self.call_GetInstanceMethod()
        self.initial_data = self.call_GetInitialDataMethod()

        response = self.call_GetBsnMethod()
        if isinstance(response, QuerySet):
            context['records'] = response

        if isinstance(response, PageDto):
            return redirect(response.get_Url())

        if isinstance(response, ContextItemDto):
            context[response.key] = response.value

        self.init_Form()

        for key, value in self.context.items():
            context[key] = value

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        self.request = request
        context["page_name"] = self.get_PageName()
        context["page_title"] = self.get_PageTitle()
        context["breadcrumb"] = self.get_Breadcrumb()
        context["toolbar"] = self.get_Toolbar()
        context['custom_param'] = self.get_CustomParams()
        context["module_key"] = self.get_ModuleKey()

        # self.set_Params(param1, param2)
        self.set_Params(kwargs)

        self.instance = self.call_GetInstanceMethod()
        # self.initial_data = self.call_GetInitialDataMethod()

        form = self.init_Form()
        if form.is_valid():
            try:
                self.data = form.cleaned_data
                response = self.call_PostBsnMethod()

                if isinstance(response, QuerySet):
                    context['records'] = response

                if isinstance(response, PageDto):
                    return redirect(response.get_Url())

                if isinstance(response, ContextItemDto):
                    context[response.key] = response.value

                for key, value in self.context.items():
                    context[key] = value

            except Exception as error:
                self.set_ErrorMessages(error)

        else:
            for key, value in self.context.items():
                context[key] = value

        return render(request, self.template_name, context)


class SecurityGuard(object):
    only_superuser = False
    only_admin = False
    security_method = None

    def validate_Security(self, _request_user):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.security_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar el metodo security_method"
            )

        return getattr(self.app_class, self.security_method)(
            self.request,
            self.param
        )

        # if self.app_class:
        #     self.app = self.app_class(_request_user)

        #     try:
        #         if self.app.is_CurrenUserAlreadyLogIn() is False:
        #             return self.app.get_UrlLogin()

        #         self.app.check_CurrenUserStatus()

        #         if self.app.should_CurrentUserRestarPassword():
        #             return self.app.get_UrlRenewPassword()

        #         if self.app.has_CurrenUserSuperuserPowers():
        #             return None

        #         if self.only_superuser:
        #             raise ValidationError(
        #                 "El Usuario debe tener permisos de Superusuario"
        #             )

        #         if self.app.has_CurrenUserAdminPowers():
        #             return None

        #         if self.only_admin:
        #             raise ValidationError(
        #                 "El Usuario debe tener permisos de Administrador"
        #             )

        #         self.app.check_CurrentUserAccessPermisionForPage(self.page_key)

        #     except Exception as error:
        #         # TODO: This message going to Log
        #         print(str(error))
        #         raise Http404

        # else:
        #     raise ImproperlyConfigured(
        #         "Favor de especificar la clase de seguridad"
        #     )


class SecurityView(SimpleView, SecurityGuard):

    def get(self, request, *args, **kwargs):
        try:
            response = self.validate_Security(request.user)
            if isinstance(response, PageDto):
                return redirect(response.get_Url())

        except Exception as e:
            raise Http404(e)

        return super(SecurityView, self).get(
            request,
            *args,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        try:
            response = self.validate_Security(request.user)
            if isinstance(response, PageDto):
                return redirect(response.get_Url())

        except Exception as e:
            raise Http404(e)

        return super(SecurityView, self).post(
            request,
            *args,
            **kwargs
        )


class SecurityFormView(FormView, SecurityGuard):

    def get(self, request, *args, **kwargs):
        response = self.validate_Security(request.user)
        if isinstance(response, PageDto):
            return redirect(response.get_Url())

        return super(SecurityFormView, self).get(
            request,
            *args,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        response = self.validate_Security(request.user)
        if isinstance(response, PageDto):
            return redirect(response.get_Url())

        return super(SecurityFormView, self).post(
            request,
            *args,
            **kwargs
        )

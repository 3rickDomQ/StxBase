# Django's Libraries
# from abc import ABC
# from abc import abstractmethod
from django.core.exceptions import ImproperlyConfigured

# Third-party Libraries
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend


class ApiView(viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    request = None
    params = {}
    app_class = None

    def set_Params(self, _request):
        self.params = _request.parser_context['kwargs']


class BaseList(object):
    list_method = None

    def get_Objects(self):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.list_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar un list_method"
            )

        return getattr(self.app_class, self.list_method)(
            self.request,
            self.params
        )


class BaseCreate(object):
    create_method = None

    def save_Object(self, _serializer):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.create_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar un create_method"
            )

        return getattr(self.app_class, self.create_method)(
            self.request,
            self.params,
            _serializer.validated_data
        )


class BaseRetrieve(object):
    retrieve_method = None

    def get_Object(self):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.retrieve_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar un retrieve_method"
            )

        return getattr(self.app_class, self.retrieve_method)(
            self.request,
            self.params
        )


class BaseUpdate(object):
    update_method = None

    def update_Object(self, _serializer):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.update_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar un update_method"
            )

        return getattr(self.app_class, self.update_method)(
            self.request,
            self.params,
            _serializer.validated_data
        )


class BaseDelete(object):
    delete_method = None

    def delete_Object(self):
        if self.app_class is None:
            raise ImproperlyConfigured(
                "Favor de especificar una app_class"
            )

        if self.delete_method is None:
            raise ImproperlyConfigured(
                "Favor de especificar un delete_method"
            )

        return getattr(self.app_class, self.delete_method)(
            self.request,
            self.params
        )


class ListApiView(ApiView, BaseList):

    def list(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        queryset = self.get_Objects()
        if queryset:
            queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CreateApiView(ApiView, mixins.CreateModelMixin, BaseCreate):

    serializer_list_class = None

    def create(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.save_Object(serializer)

        if self.serializer_list_class:
            serializer = self.serializer_list_class(instance)

        else:
            serializer = self.get_serializer(instance)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ListCreateApiView(
    ApiView,
    mixins.CreateModelMixin,
    BaseList,
    BaseCreate
):
    serializer_list_class = None

    def list(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)
        queryset = self.get_Objects()

        if queryset:
            queryset = self.filter_queryset(queryset)

        if self.serializer_list_class:
            serializer = self.serializer_list_class(queryset, many=True)

        else:
            serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.save_Object(serializer)

        if self.serializer_list_class:
            serializer = self.serializer_list_class(instance)
        else:
            serializer = self.get_serializer(instance)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class RetrieveApiView(ApiView, mixins.RetrieveModelMixin, BaseRetrieve):

    def retrieve(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        instance = self.get_Object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateApiView(
    ApiView,
    mixins.UpdateModelMixin,
    BaseRetrieve,
    BaseUpdate
):

    def update(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        partial = kwargs.pop('partial', False)
        instance = self.get_Object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.update_Object(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class DestroyApiView(ApiView, mixins.DestroyModelMixin, BaseDelete):

    def destroy(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        self.instance = self.get_Object()
        self.delete_Object()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RUDApiView(
    ApiView,
    BaseRetrieve,
    BaseUpdate,
    BaseDelete,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_retrieve_class = None

    def retrieve(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        instance = self.get_Object()

        if self.serializer_retrieve_class:
            serializer = self.serializer_retrieve_class(instance)
        else:
            serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        partial = kwargs.pop('partial', False)
        instance = self.get_Object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.update_Object(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)
        self.instance = self.get_Object()
        self.delete_Object()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RetrieveUpdateApiView(
    ApiView,
    BaseRetrieve,
    BaseUpdate,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    serializer_retrieve_class = None

    def retrieve(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        instance = self.get_Object()
        if self.serializer_retrieve_class:
            serializer = self.serializer_retrieve_class(instance)
        else:
            serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        partial = kwargs.pop('partial', False)
        instance = self.get_Object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.update_Object(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class RetrieveDestroyApiView(
    ApiView,
    BaseRetrieve,
    BaseDelete,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):

    def retrieve(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)

        instance = self.get_Object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.request = request
        self.set_Params(request)
        self.instance = self.get_Object()
        self.delete_Object()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SecurityApiView(ApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityListApiView(ListApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityListCreateApiView(ListCreateApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityCreateApiView(CreateApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityRetrieveApiView(RetrieveApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityUpdateApiView(UpdateApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityDestroyApiView(DestroyApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityRUDApiView(RUDApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityRetrieveUpdateApiView(RetrieveUpdateApiView):
    # permission_classes = (IsAuthenticated, )
    pass


class SecurityRetrieveDestroyApiView(RetrieveDestroyApiView):
    # permission_classes = (IsAuthenticated, )
    pass

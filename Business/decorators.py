# Python's Libriares
from functools import wraps

# Own's Libraries
from Utils.errors import SecurityError


def controller(permission):
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            # service = PermissionService()
            # service.check_Integrity(permission)
            permisos = list(args[0].user.position.permission_set.all())
            compare = [(item.module.key, item.action.key) for item in permisos]
            if (permission in compare) is not True:
                raise SecurityError("No cuenta con los permisos necesarios")

            return func(request, *args, **kwargs)
        return inner
    return decorator

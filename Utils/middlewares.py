# Python's Libraries
import time
import pytz
from datetime import datetime

# Django's Libraries
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

SESSION_TIMEOUT_KEY = "_session_init_timestamp_"


class SessionControlMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, "session") or request.session.is_empty():
            return

        init_time = request.session.setdefault(
            SESSION_TIMEOUT_KEY, time.time()
        )

        expire_seconds = getattr(
            settings, "SESSION_EXPIRE_SECONDS", settings.SESSION_COOKIE_AGE
        )

        session_is_expired = time.time() - init_time > expire_seconds

        if session_is_expired:
            request.session.flush()
            return redirect_to_login(next=request.path)

        expire_since_last_activity = getattr(
            settings, "SESSION_EXPIRE_AFTER_LAST_ACTIVITY", False
        )
        grace_period = getattr(
            settings, "SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD", 1
        )

        if expire_since_last_activity \
           and time.time() - init_time > grace_period:
            request.session[SESSION_TIMEOUT_KEY] = time.time()


class OnlyOneSessionMiddleware:

    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            stored_session_key = request.user.session_key

            # if there is a stored_session_key  in our database and it is
            # different from the current session, delete the stored_session_key
            # session_key with from the Session table
            if stored_session_key \
                and stored_session_key \
                    != request.session.session_key:
                try:
                    session = Session.objects.get(
                        session_key=stored_session_key
                    )
                    session.delete()
                except ObjectDoesNotExist:
                    print("No existe sesión activa")

            request.user.session_key = \
                request.session.session_key

            request.user.last_activity = \
                datetime.fromtimestamp(
                    request.session[SESSION_TIMEOUT_KEY],
                    tz=pytz.utc
                )

            request.user.save()
            print("Se crea sessión")

        response = self.get_response(request)

        # This is where you add any extra code to be executed for each request/response after
        # the view is called.
        # For this tutorial, we're not adding any code so we just return the response

        return response

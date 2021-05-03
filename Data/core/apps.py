# Django's Libraries
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = "Seguridad"

    def ready(self):
        import Business.signals

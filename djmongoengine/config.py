from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from mongoengine import connection


class DjMongoEngineConfig(AppConfig):

    name = "djmongoengine"

    def ready(self):
        if not hasattr(settings, "MONGODB_DATABASES"):
            raise ImproperlyConfigured("Missing `MONGODB_DATABASES` in settings.py")

        for alias, conn_settings in settings.MONGODB_DATABASES.items():
            connection.register_connection(alias, **conn_settings)

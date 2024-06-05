from django.apps import AppConfig
from django.db import connections


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self):
        # signal to create database and migrate required apps
        import main_app.signals

        # load all databases when the application is restarted
        from .models import Tenant

        for tenant in Tenant.objects.all():
            connections.databases[f"{tenant.subdomain}"] = {
                "ENGINE": "django.db.backends.postgresql",
                "HOST": "localhost",
                "NAME": f"{tenant.subdomain}",
                "USER": "postgres",
                "PASSWORD": "42213",
                "PORT": "5432",
                "ATOMIC_REQUESTS": False,
                "TIME_ZONE": "UTC",
                "CONN_MAX_AGE": 0,
                "CONN_HEALTH_CHECKS": True,
                "OPTIONS": {},
                "AUTOCOMMIT": True,
            }

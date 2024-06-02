from django.apps import AppConfig
from django.db import connections


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self):
        import main_app.signals
        from .models import Tenant

        for tenant in Tenant.objects.all():

            connections.databases[tenant.subdomain] = {
                "ENGINE": "django.db.backends.postgresql",
                "HOST": "localhost",
                "NAME": f"{tenant.subdomain}",
                "USER": "postgres",
                "PASSWORD": "42213",
                "PORT": "5432",
                "ATOMIC_REQUESTS": False,
            }

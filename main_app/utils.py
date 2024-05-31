from django.db import connection
from django.conf import settings


def create_tenant_database(tenant):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE {tenant.subdomain}")
        cursor.execute(
            f"CREATE USER {tenant.username} WITH PASSWORD '{tenant.password}'"
        )
        cursor.execute(
            f"GRANT ALL PRIVILEGES ON DATABASE {tenant.subdomain} TO {tenant.username}"
        )

        settings.DATABASES[f"{tenant.subdomain}"] = {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "localhost",
            "NAME": f"{tenant.subdomain}",
            "USER": f"{tenant.username}",
            "PASSWORD": f"{tenant.password}",
            "PORT": "5432",
        }

import traceback
import psycopg
import threading
import os
import django

from django.db import connections
from django.core.management import call_command
from django.conf import settings


def create_tenant_database(tenant):
    connection = psycopg.connect(
        dbname=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        host=settings.DATABASES["default"]["HOST"],
        port=settings.DATABASES["default"]["PORT"],
    )
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {tenant.subdomain};")
    except Exception as e:
        print(f"error {e}")
    # cursor.execute(f"CREATE USER {tenant.username} WITH PASSWORD '{tenant.password}'")
    # cursor.execute(
    #     f"GRANT ALL PRIVILEGES ON DATABASE {tenant.subdomain} TO {tenant.username}"
    # )
    cursor.close()
    connection.close()

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


def apply_migrations_to_tenant(tenant):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    django.setup()

    try:
        call_command("migrate", database=tenant.subdomain, app_label="tenant_app")
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}")


_thread_locals = threading.local()


def get_current_request():
    return getattr(_thread_locals, "db_name", None)


def set_current_request(db_name):
    _thread_locals.db_name = db_name

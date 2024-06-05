from django.db import connections
from .utils import get_current_request


class CustomDatabaseRouter:

    # tenant specific apps
    route_app_label = {
        "tenant_app",
    }

    def db_for_read(self, model, **hints):
        db_name = get_current_request()
        if db_name:
            if model._meta.app_label in self.route_app_label:
                return db_name
        return "default"

    def db_for_write(self, model, **hints):
        db_name = get_current_request()
        if db_name:
            if model._meta.app_label in self.route_app_label:
                return db_name
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        db_name = get_current_request()
        if db_name:
            if obj1._state.db == db_name and obj2._state.db == db_name:
                return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # migrations on all databases
        return True


# class TenantRouter:
#     def db_for_read(self, model, **hints):
#         tenant = hints.get("tenant")
#         if tenant:
#             return tenant.subdomain
#         return None

#     def db_for_write(self, model, **hints):
#         tenant = hints.get("tenant")
#         if tenant:
#             return tenant.subdomain
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         tenant = hints.get("tenant")
#         if tenant:
#             return tenant.subdomain == hints.get("tenant").subdomain
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         # Ensure migrations only run on the default database
#         return db == "default"

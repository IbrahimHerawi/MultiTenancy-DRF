from .utils import get_current_request


class CustomDatabaseRouter:
    def db_for_read(self, model, **hints):
        db_name = get_current_request()
        if db_name:
            return "db_name"
        return "default"

    def db_for_write(self, model, **hints):
        db_name = get_current_request()
        if db_name:
            return "db_name"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are in the same database.
        db_obj1 = hints.get("database", None)
        db_obj2 = hints.get("database", None)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations on all databases
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

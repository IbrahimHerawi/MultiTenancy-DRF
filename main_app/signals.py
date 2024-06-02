from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tenant
from .utils import create_tenant_database, apply_migrations_to_tenant


@receiver(post_save, sender=Tenant)
def create_resources_for_new_tenant(sender, instance, created, **kwargs):
    create_tenant_database(instance)
    apply_migrations_to_tenant(instance)

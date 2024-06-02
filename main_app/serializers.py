from rest_framework import serializers

from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = (
            "username",
            "email",
            "password",
            "facility_name",
            "subdomain",
        )

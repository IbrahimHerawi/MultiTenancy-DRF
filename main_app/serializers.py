from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import Tenant


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True)
    facility_name = serializers.CharField(max_length=100)
    subdomain = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Tenant
        fields = (
            "username",
            "email",
            "facility_name",
            "subdomain",
            "password1",
            "password2",
        )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["username"] = self.validated_data.get("username")
        data["email"] = self.validated_data.get("email")
        data["facility_name"] = self.validated_data.get("facility_name")
        data["subdomain"] = self.validated_data.get("subdomain")
        return data

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = Tenant.objects.create_user(
            username=cleaned_data.get("username"),
            email=cleaned_data.get("email"),
            password=cleaned_data.get("password1"),
            facility_name=cleaned_data.get("facility_name"),
            subdomain=cleaned_data.get("subdomain"),
        )

        return user


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

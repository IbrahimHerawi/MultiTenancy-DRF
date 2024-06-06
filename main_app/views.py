from rest_framework import viewsets
from dj_rest_auth.views import LoginView
from rest_framework.authtoken.models import Token

from .serializers import TenantSerializer
from .models import Tenant


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class CustomLoginView(LoginView):
    def get_response(self):
        original_response = super().get_response()
        tenant = self.request.user
        subdomain = tenant.subdomain
        original_response.data["subdomain"] = subdomain

        return original_response

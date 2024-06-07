from rest_framework import viewsets
from dj_rest_auth.views import LoginView

from .serializers import TenantSerializer
from .models import Tenant


# a view for the admin of the application to manipulate all tenants
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


# cusotm log in to include the subdomain in the response
class CustomLoginView(LoginView):
    def get_response(self):
        original_response = super().get_response()
        tenant = self.request.user
        subdomain = tenant.subdomain
        original_response.data["subdomain"] = subdomain

        return original_response

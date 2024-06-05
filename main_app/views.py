from rest_framework import viewsets, response
from rest_framework.decorators import api_view
from .utils import get_current_request

from .serializers import TenantSerializer
from .models import Tenant


@api_view(["GET"])
def index(request):
    subdomain = get_current_request()
    return response.Response({"subdomain": subdomain})


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

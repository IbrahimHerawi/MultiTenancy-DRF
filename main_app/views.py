from rest_framework import viewsets, generics
from django.db import transaction

from .serializers import TenantSerializer
from .models import Tenant


class TenantCreateView(generics.CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantListView(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


# class TenantViewSet(viewsets.ModelViewSet):
#     queryset = Tenant.objects.all()
#     serializer_class = TenantSerializer

#     @transaction.non_atomic_requests
#     def list(self, request, *args, **kwargs):
#         # Non-atomic logic here
#         return super().list(request, *args, **kwargs)

#     @transaction.non_atomic_requests
#     def retrieve(self, request, *args, **kwargs):
#         # Non-atomic logic here
#         return super().retrieve(request, *args, **kwargs)

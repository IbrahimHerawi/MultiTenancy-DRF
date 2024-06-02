from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import TenantListView, TenantCreateView


# router = SimpleRouter()
# router.register("tenants", TenantViewSet, basename="tenants")


urlpatterns = [
    path("tenants/", TenantListView.as_view(), name="tenant-list"),
    path("tenant/create/", TenantCreateView.as_view(), name="tenant-new"),
    # path("", include(router.urls)),
]

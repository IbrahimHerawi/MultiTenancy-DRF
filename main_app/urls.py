from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import TenantViewSet, index


router = SimpleRouter()
router.register("tenants", TenantViewSet, basename="tenants")


urlpatterns = [
    path("subdomain/", index, name="subdomain"),
    path("", include(router.urls)),
]

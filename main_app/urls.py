from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import TenantViewSet, CustomLoginView


router = SimpleRouter()
router.register("tenants", TenantViewSet, basename="tenants")


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("", include(router.urls)),
]

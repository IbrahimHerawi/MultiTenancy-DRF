from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import EmployeeViewSet


router = SimpleRouter()
router.register("", EmployeeViewSet, basename="employee")


urlpatterns = [
    path("", include(router.urls)),
]

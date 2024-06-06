from rest_framework import viewsets, permissions

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from .models import Department
from rest_framework import generics, permissions
from .serializer import DepartmentSerializer


class DepartmentList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AddDepartment(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

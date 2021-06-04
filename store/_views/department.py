from ..models import Department
from rest_framework import generics, permissions
from ..serializers.department import DepartmentSerializer


class DepartmentList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AddDepartment(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

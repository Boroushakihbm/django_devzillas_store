from .models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['title', 'description', 'parent_department', 'insert_date', 'update_date', 'user', ]

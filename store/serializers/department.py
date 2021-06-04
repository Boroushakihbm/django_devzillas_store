from ..models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    parent_department = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Department
        fields = ['title',
                  'description',
                  'parent_department_id',
                  'parent_department',
                  'insert_date',
                  'update_date',
                  'user_id',
                  'user', ]

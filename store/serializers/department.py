from ..models.department import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    parent_department = serializers.StringRelatedField(many=False)
    parent_department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),
                                                              source='parent_department',
                                                              allow_null=True, read_only=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Department
        fields = ['id',
                  'title',
                  'description',
                  'parent_department_id',
                  'parent_department',
                  'insert_date',
                  'update_date',
                  'user',
                  'user_id']

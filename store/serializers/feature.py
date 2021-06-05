from ..models import Feature, Department
from rest_framework import serializers


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.StringRelatedField(many=False)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),
                                                       source='department')

    class Meta:
        model = Feature
        fields = ['title',
                  'description',
                  'final_price',
                  'price',
                  'discount',
                  'rate',
                  'insert_date',
                  'update_date',
                  'department_id',
                  'department',
                  'user_id', ]

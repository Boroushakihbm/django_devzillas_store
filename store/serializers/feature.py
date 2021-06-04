from ..models import Feature
from rest_framework import serializers


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

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
                  'user_id',
                  'user',
                  'department_id',
                  'department', ]

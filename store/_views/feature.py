from ..models import Feature
from rest_framework import generics, permissions
from ..serializers.feature import FeatureSerializer


class FeatureList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class AddFeature(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

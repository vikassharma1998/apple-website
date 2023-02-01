from rest_framework import serializers
from .models import IphoneModels, IphoneFeatures


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IphoneModels
        fields = '__all__'

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IphoneFeatures
        fields = '__all__'
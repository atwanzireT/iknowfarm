from .models import *
from rest_framework import serializers

class CropSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('english','arabic', 'lugbara', 'image')

class LivestockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = ('english','arabic', 'lugbara', 'image')

class CropTranslationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('arabic', 'lugbara')

class LivestockTranslationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = ('arabic', 'lugbara')


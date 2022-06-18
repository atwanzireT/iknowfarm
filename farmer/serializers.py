from rest_framework import serializers
from .models import *

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ("name", "age", "gender", "village", "phonenumber", "pin", "codesent", "status", "expiry", "recommender", "group", "farmer_type")


class FarmerGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = FarmerGroup
        fields = ("name", "pin", "group_type", "female_farmers", "male_farmers", "village", "phonenumber", "limit", "recommender", "status", "ëxpiry" )


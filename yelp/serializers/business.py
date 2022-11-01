from rest_framework import serializers
from yelp.models import Business


class ListBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ["business_id","name","address","city","state",]

class RetrieveBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class GetBusinessSerializer(serializers.Serializer):
    business_id = serializers.CharField(max_length=22)
from rest_framework import serializers
from yelp.models import YelpUser

class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpUser
        fields = ["user_id","name","review_count",]

class RetrieveUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpUser
        fields = '__all__'


class GetUsersSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=22)
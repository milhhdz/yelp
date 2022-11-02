from rest_framework import serializers
from yelp.models import Review

class ListReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_id","stars",]
        # fields = ["review_id","user_id","business_id","stars",]

class RetrieveReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class GetReviewsSerializer(serializers.Serializer):
    review_id = serializers.CharField(max_length=22)
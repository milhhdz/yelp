from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.pagination import LimitOffsetPagination

from yelp.models import Review
from yelp.serializers.reviews import ListReviewsSerializer, RetrieveReviewsSerializer, GetReviewsSerializer

class ListReviewsView(ListAPIView):
    # queryset = Review.objects.only("review_id","user_id","business_id","stars").all()
    queryset = Review.objects.only("review_id","stars").all()
    serializer_class = ListReviewsSerializer
    pagination_class = LimitOffsetPagination


class RetrieveReviewsView(APIView):
    def get(self, request):
        serializer = GetReviewsSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        review_id = serializer.data["review_id"]

        try:

            review = Review.objects.select_related(
                'user_id',
                'business_id'
            ).only(
                'review_id','stars','date','text','useful','funny','cool',
                'user_id__user_id', 'user_id__name',
                'business_id__business_id', 'business_id__name'
            ).get(review_id=review_id)
        except:
            return Response({"errors":[{"review":"not found"}]}, status=HTTP_404_NOT_FOUND)

        review_d = RetrieveReviewsSerializer(review).data

        response_data = {}
        for k, v in review_d.items():
            if k == "user_id":
                response_data[k] = {"user_id":review.user_id.user_id,"name":review.user_id.name} if review.user_id else ""
            elif k == "business_id":
                response_data[k] = {"business_id":review.business_id.business_id,"name":review.business_id.name} if review.business_id else ""
            else:
                response_data[k] = v

        return Response(response_data, status=HTTP_200_OK)
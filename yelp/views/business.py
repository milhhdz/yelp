from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.pagination import LimitOffsetPagination

from yelp.models import Business
from yelp.serializers.business import ListBusinessSerializer, RetrieveBusinessSerializer, GetBusinessSerializer

class ListBusinessView(ListAPIView):
    queryset = Business.objects.only("business_id","name","address","city","state").all()
    serializer_class = ListBusinessSerializer
    pagination_class = LimitOffsetPagination

class RetrieveBusinessView(APIView):
    def get(self, requets):
        print(requets.data)
        serializer = GetBusinessSerializer(data=requets.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        business_id = serializer.data["business_id"]

        try:
            business = Business.objects.get(business_id=business_id)
        except:
            return Response({"errors":[{"business":"not found"}]}, status=HTTP_404_NOT_FOUND)

        business = RetrieveBusinessSerializer(business)
        return Response(business.data, status=HTTP_200_OK)
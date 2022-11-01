from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
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
    def get(self, requets, business_id=None):

        try:
            business = Business.objects.get(business_id=business_id)
        except:
            return Response({"business":"not found"}, status=HTTP_404_NOT_FOUND)

        business = RetrieveBusinessSerializer(business)
        return Response(business.data, status=HTTP_200_OK)
        

    # def get(self, request):
    #     query = Business.objects.only("business_id","name","address","city","state").all()
    #     serializer = ListBusinessSerializer(query, many=True)

    #     return Response(serializer.data, status=HTTP_200_OK)

# class ListBusinessView(APIView):
#     def get(self, request):
#         try:
#             query = 
#         except:
#             pass
#         query = Business.objects.only("business_id","name","address","city","state").all()
#         serializer = ListBusinessSerializer(query, many=True)

#         return Response(serializer.data, status=HTTP_200_OK)
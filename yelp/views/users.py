from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.pagination import LimitOffsetPagination

from yelp.models import YelpUser
from yelp.serializers.users import ListUsersSerializer, RetrieveUsersSerializer, GetUsersSerializer

class ListUsersView(ListAPIView):
    queryset = YelpUser.objects.only("user_id","name","review_count").all()
    serializer_class = ListUsersSerializer
    pagination_class = LimitOffsetPagination

class RetrieveUsersView(APIView):
    offset = 0
    next_ = 0
    previous_ = 0
    def get(self, request):
        serializer = GetUsersSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        user_id = serializer.data["user_id"]

        try:
            user = YelpUser.objects.get(user_id=user_id)
        except:
            return Response({"user":"not found"}, status=HTTP_404_NOT_FOUND)

        friends = [id_.replace(" ", "") for id_ in user.friends.split(",")]
        users = RetrieveUsersSerializer(user).data
        
        response_data = {}
        for k, v in users.items():
            response_data[k] = v
        if len(request.query_params.keys()) != 0:
            params_is_valid = self.validated_params()
            if params_is_valid != True:
                return params_is_valid
            else:
                response_data["friends"] = self.get_friends_related(friends, self.offset)
        else:
            response_data["friends"] = self.get_friends_related(friends)
        
        response_data["elite"] = [int(year.replace(" ", "")) for year in response_data["elite"].split(",")]
        
        return Response(response_data, status=HTTP_200_OK)

    def validated_params(self):
        try:
            offset = (self.request.query_params.get("offset"))
        except:
            return Response({"errors":[{"params":"is not valid"}]}, status=HTTP_400_BAD_REQUEST)
        
        if not offset.isdigit():
            return Response({"errors":[{"offset":"should be a number"}]}, status=HTTP_400_BAD_REQUEST)

        self.offset = int(offset)
        
        return True
    
    def get_friends_related(self, friends_list: list, offset: int = 20):
        start = offset - 20
        response_friends = {
            "count": len(friends_list),
            "next": self.get_next_page(offset, len(friends_list)),
            "previous": self.get_previous_page(offset),
            "results": self.get_paginate_friends(friends_list, start, offset)
        }

        return response_friends

    def get_previous_page(self, offset):
        subtract_ = offset - 20
        self.previous_ = subtract_
        if subtract_ == 20:
            return self.get_url()
        if subtract_ == 0:
            return ""
        if subtract_ > 20:
            return f"{self.get_url()}?offset={subtract_}"
        
    
    def get_next_page(self, offset, limit: int = 0):
        sum_ = offset + 20
        self.next_ = sum_
        if limit < sum_:
            return f"{self.get_url()}?offset={limit}"
        return f"{self.get_url()}?offset={sum_}"
    
    def get_url(self):
        if '?' in self.request.build_absolute_uri():
            return self.request.build_absolute_uri().split("?")[0]
        else:
            return self.request.build_absolute_uri()
    
    def get_paginate_friends(self, friends_list, start, finish):

        friends = YelpUser.objects.values("user_id", "name").filter(user_id__in=friends_list[start:finish])

        response_friends = []
        for friend in friends:
            response_friends.append( {"user_id": friend["user_id"], "name": friend["name"]} )

        return response_friends

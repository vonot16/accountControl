from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import billsCategory
from ..models import User
from ..serializers import BillsCategorySerializer

from ..utils import checkUserLoggedIn


@api_view(['POST'])
def create(request):
    data = JSONParser().parse(request)

    owner_user = User.objects.get(user_id=data['owner_user'])
    if owner_user is None:
        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
    if checkUserLoggedIn(request).status_code != 200:
        return checkUserLoggedIn(request)

    serializer = BillsCategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


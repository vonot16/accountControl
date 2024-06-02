from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt, datetime 

from ..models import User
from ..serializers import UserSerializer

@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    email = data['email']
    password = data['password']
    user = User.objects.get(email=email)
    if user is None or not user.check_password(password):
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    payload = {
        'user_id': user.user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    Response().set_cookie('app_user_token', token, httponly=True)

    return Response({'message': 'User logged in', 'token':token}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def logout(request):
    response = Response()
    try:
        response.delete_cookie(key='app_user_token')
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'User not logged out'}, status=status.HTTP_400_BAD_REQUEST)
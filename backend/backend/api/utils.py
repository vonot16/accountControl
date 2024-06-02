from rest_framework import status
from rest_framework.response import Response
import jwt, datetime

def checkUserLoggedIn(request):
    token = request.COOKIES.get('app_user_token')
    print(token)
    if token is None:
        return Response({'message': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return Response({'message': 'User logged in', 'user':payload['user_id']}, status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError:
        return Response({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)


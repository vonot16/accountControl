from .models import User
from .models import Bills
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

    def create(self, validated_data):
        try:
            owner_user = User.objects.get(user_id=validated_data['owner_user'])
            if owner_user is None:
                return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
            
            login_response = checkUserLoggedIn(request)
            if login_response.status_code != 200:
                return login_response
            if login_response.data['user'] != owner_user.user_id:
                return Response({'message': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'message': 'Operation not allowed'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.Meta.model(owner_user=owner_user, **validated_data)
        instance.save()

        return instance
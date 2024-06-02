from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .models import Bills
from .models import billsCategory


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
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class BillsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = billsCategory
        fields = '__all__'

    def create(self, validated_data):

        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
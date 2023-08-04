from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'age', 'gender']
        extra_kwargs = {'password': {'write_only': True}}


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         def create(self, validated_data):
#             user= User.objects.create(username = validated_data['username'])
#             user.set_password(validated_data['password'])
#             user.save()
#             return user


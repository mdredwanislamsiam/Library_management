from rest_framework import serializers
from users.models import User 
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth.models import Group 

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta): 
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class CustomUserSerializer(UserSerializer): 
    class Meta(UserSerializer.Meta): 
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class UserSerializer(serializers.ModelSerializer): 
    password = serializers.CharField()
    class Meta: 
        model = User
        fields = ['id', 'first_name', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
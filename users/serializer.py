from rest_framework import serializers
from users.models import User 



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
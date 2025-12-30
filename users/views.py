from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializer import UserSerializer
from rest_framework import permissions


class UserViewSet(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]    
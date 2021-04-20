from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class StudentuserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.Studentuser
        fields = ('id', 'email', 'username', 'password',)

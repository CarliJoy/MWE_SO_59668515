from rest_framework import serializers, generics
from Usersapi.models import UserData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

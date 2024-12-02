from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password

   
class UserModelSerializer(serializers.ModelSerializer):   
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']     
class UserProfileSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required = True, write_only = True,)
    email = serializers.CharField(required = True)

    class Meta:
        model = UserModel
        fields = ['id', 'password', 'email']
    def create(self, validated_data):
        validated_data['password']= make_password(validated_data.get('password'))
        return super(UserProfileSerializer, self).create(validated_data)
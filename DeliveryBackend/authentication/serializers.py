"""Serializer class for User account"""
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Rider, User
from payments.models import UserWallet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_rider', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserWallet.objects.create(user=user)
        return user
    
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ['user', 'mobile_number', 'location', 'license_upload']
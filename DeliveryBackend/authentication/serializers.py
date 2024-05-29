"""Serializer class for User account"""
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Rider, Customer




class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password')
        # Ensure the password is write-only and not included in responses
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to properly hash the password
    def create(self, validated_data):
        password = validated_data.pop('password')
        User.objects.create_user(password=password, **validated_data)
        customer = Customer.objects.create_user(password=password, **validated_data)
        return customer
    
class RiderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('first_name','last_name', 'mobile_number', 'email', 'location','password')

        # Ensure the password is write-only and not included in responses
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to properly hash the password
    def create(self, validated_data):
        password = validated_data.pop('password')
        User.objects.create_user(password=password, **validated_data)
        rider = Rider.objects.create_user(password=password, **validated_data)
        return rider
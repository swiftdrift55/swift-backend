"""Serializer class for User account"""
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Rider, Customer




class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password', 'role')
        # Ensure the password is write-only and not included in responses
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to properly hash the password
    def create(self, validated_data):
        role = validated_data.pop('role', 'customer')
        password = validated_data.pop('password')
        User.objects.create_user(password=password, **validated_data)
        customer = Customer.objects.create_user(password=password, **validated_data)
        group, created = Group.objects.get_or_create(name=role)
        customer.groups.add(group)
        return customer
    
class RiderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('first_name','last_name', 'mobile_number', 'email', 'location','password', 'role')

        # Ensure the password is write-only and not included in responses
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to properly hash the password
    def create(self, validated_data):
        role = validated_data.pop('role', 'rider')
        password = validated_data.pop('password')
        User.objects.create_user(password=password, **validated_data)
        rider = Rider.objects.create_user(password=password, **validated_data)
        group, created = Group.objects.get_or_create(name=role)
        rider.groups.add(group)
        return rider
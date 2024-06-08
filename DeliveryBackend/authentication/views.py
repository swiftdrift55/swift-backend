from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Rider
from .serializers import CustomerRegisterSerializer, RiderRegisterSerializer
from django.contrib.auth.models import User
from django.http import Http404


class CustomerRegistration(generics.CreateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomerRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        response_data = {
            'id': customer.id,
            'email': customer.email,
            'username': customer.username,
            'mobile_number': customer.mobile_number
        }
        return Response(response_data)


class RiderRegistration(generics.CreateAPIView):
    queryset = Rider.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RiderRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rider = serializer.save()
        response_data = {
            'id': rider.id,
            'email': rider.email,
            'username': rider.username,
            'first_name': rider.first_name,
            'last_name': rider.last_name,
            'mobile_number': rider.mobile_number,
            'location': rider.location,
        }
        return Response(response_data)
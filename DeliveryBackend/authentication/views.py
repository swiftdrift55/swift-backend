from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerRegisterSerializer, RiderRegisterSerializer
from django.contrib.auth.models import User
from django.http import Http404


class CustomerRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomerRegisterSerializer


class RiderRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RiderRegisterSerializer
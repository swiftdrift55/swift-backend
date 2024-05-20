from django.shortcuts import render
from requests import Response
from rest_framework import generics
from .models import Rider, User
from .serializers import RiderSerializer, UserSerializer


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    


class RiderSignupView(generics.CreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
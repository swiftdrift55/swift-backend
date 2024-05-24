from django.shortcuts import render
from requests import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .models import Rider, User
from .serializers import RiderSerializer, UserSerializer


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    


class RiderSignupView(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RiderSerializer
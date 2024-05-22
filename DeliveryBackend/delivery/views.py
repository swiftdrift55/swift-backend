from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .models import DeliveryRequest
from .serializers import DeliveryRequestSerializer
from django.contrib.auth.decorators import login_required


class DeliveryRequestListCreateView(generics.ListCreateAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DeliveryRequestRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
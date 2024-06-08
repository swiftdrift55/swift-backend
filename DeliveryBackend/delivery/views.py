from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import DeliveryRequest
from .serializers import DeliveryRequestSerializer, RiderDeliveryRequestSerializer
from django.contrib.auth.decorators import login_required


class DeliveryRequestListCreateView(generics.ListCreateAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DeliveryRequestRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DeliveryRequestDestroyView(generics.DestroyAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class RiderDeliveryRequestListView(generics.ListAPIView):
    serializer_class = RiderDeliveryRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        rider_id = self.kwargs.get('rider_id')
        return DeliveryRequest.objects.filter(assigned_rider_id=rider_id)

class CustomerDeliveryRequestsView(generics.ListAPIView):
    serializer_class = DeliveryRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return DeliveryRequest.objects.filter(customer__id=customer_id)
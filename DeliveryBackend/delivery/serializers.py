from rest_framework import serializers
from .models import DeliveryRequest


class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ('customer', 'item_name', 'pickup_address', 'sender_location', 'receiver_name', 'receiver_mobile_number', 'payment_status', 'payment_value', 'status')
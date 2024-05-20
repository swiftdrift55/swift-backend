from rest_framework import serializers
from .models import DeliveryRequest


class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = '__all__'
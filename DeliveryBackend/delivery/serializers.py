from rest_framework import serializers
from .models import DeliveryRequest

class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ('customer', 'item_name', 'pickup_address', 'sender_location', 'receiver_name', 'receiver_mobile_number', 'request_date', 'payment_status', 'payment_value', 'status')

    def create(self, validated_data):
        # Convert the request_date to a string in the desired format (e.g., "YYYY-MM-DD")
        request_date = validated_data.get('request_date', None)
        if request_date:
            validated_data['request_date'] = request_date.strftime('%Y-%m-%d')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Convert the request_date to a string in the desired format (e.g., "YYYY-MM-DD")
        request_date = validated_data.get('request_date', None)
        if request_date:
            validated_data['request_date'] = request_date.strftime('%Y-%m-%d')
        return super().update(instance, validated_data)

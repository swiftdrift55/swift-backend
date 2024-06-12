from rest_framework import serializers
from .models import DeliveryRequest

class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ('customer', 'item_name', 'pickup_address', 'sender_location', 'receiver_name', 'receiver_mobile_number', 'sender_email','request_date', 'payment_status', 'payment_value', 'status')

    def create(self, validated_data):
        request_date = validated_data.get('request_date', None)
        if request_date:
            validated_data['request_date'] = request_date.strftime('%Y-%m-%d')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request_date = validated_data.get('request_date', None)
        if request_date:
            validated_data['request_date'] = request_date.strftime('%Y-%m-%d')
        return super().update(instance, validated_data)
    

class RiderDeliveryRequestSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()

    class Meta:
        model = DeliveryRequest
        fields = ['date_of_delivery', 'pickup_address', 'message']

    def create(self, validated_data):
        # Ensure the date_of_delivery is formatted correctly
        date_of_delivery = validated_data.get('date_of_delivery', None)
        if date_of_delivery:
            validated_data['date_of_delivery'] = date_of_delivery.strftime('%Y-%m-%d')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Ensure the date_of_delivery is formatted correctly
        date_of_delivery = validated_data.get('date_of_delivery', None)
        if date_of_delivery:
            validated_data['date_of_delivery'] = date_of_delivery.strftime('%Y-%m-%d')
        return super().update(instance, validated_data)

    def get_message(self, obj):
        return "You have been assigned to this delivery request."
    

class CustomerSuccesfulDelivery(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        field = ['date_of_delivery', 'pickup_address', 'message']

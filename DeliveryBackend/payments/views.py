from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render
from payments.models import Payment
from .serializers import *

# Create your views here.
class InitiatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            payment = serializer.save()
            pk = settings.PAYSTACK_PUBLIC_KEY
            serialized_payment_data = serializer.data
            serialized_payment = PaymentSerializer(payment).data
            
            # Remove 'ref' field from the serialized data
            serialized_payment_data.pop('ref', None)  # Serialize the payment object excluding 'ref' field
            ref = payment.ref 
            context = {
                'payment': serialized_payment,
                'paystack_pub_key': pk,
                'ref': ref,
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ref, *args, **kwargs):
        try:
            payment = Payment.objects.get(ref=ref)
        except Payment.DoesNotExist:
            return Response({"detail": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        verified = payment.verify_payment()

        if verified:
            return Response({"detail": "Payment verified"}, status=status.HTTP_200_OK)

        return Response({"detail": "Payment verification failed."}, status=status.HTTP_400_BAD_REQUEST)
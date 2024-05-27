import hmac
import hashlib
import json
from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views import View
from .models import Payment
from .serializers import PaymentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class InitiatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            payment = serializer.save()
            pk = settings.PAYSTACK_PUBLIC_KEY

            serialized_payment_data = serializer.data
            ref = payment.ref
            context = {
                'payment': serialized_payment_data,
                'paystack_pub_key': pk,
                'ref': ref,
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class PaystackWebhookView(View):
    
    def post(self, request, *args, **kwargs):
        payload = request.body
        signature = request.headers.get('x-paystack-signature')
        secret_key = settings.PAYSTACK_SECRET_KEY

        if not self.verify_signature(payload, signature, secret_key):
            return JsonResponse({'status': 'unauthorized'}, status=401)

        event = json.loads(payload)
        if event['event'] == 'charge.success':
            self.handle_successful_payment(event['data'])

        return JsonResponse({'status': 'success'}, status=200)
    
    def verify_signature(self, payload, signature, secret_key):
        computed_signature = hmac.new(
            secret_key.encode(), payload, hashlib.sha512
        ).hexdigest()
        return hmac.compare_digest(computed_signature, signature)

    def handle_successful_payment(self, data):
        ref = data['reference']
        try:
            payment = Payment.objects.get(ref=ref)
            payment.verified = True
            payment.save()
        except Payment.DoesNotExist:
            pass  # Handle the case where the payment is not found

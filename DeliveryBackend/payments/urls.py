from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/', views.InitiatePaymentView.as_view(), name='initiate_payment'),
    path('webhook/', views.PaystackWebhookView.as_view(), name='paystack_webhook'),
]
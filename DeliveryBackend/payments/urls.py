from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.PaystackWebhookView.as_view(), name='paystack_webhook'),
]
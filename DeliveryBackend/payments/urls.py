from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/', views.InitiatePaymentView.as_view(), name='initiate_payment'),
    path('verify-payment/<str:ref>/', views.VerifyPaymentView.as_view(), name='verify_payment'),
]
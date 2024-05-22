from django.urls import path
from .views import DeliveryRequestListCreateView, DeliveryRequestRetrieveUpdateView

urlpatterns = [
    path('request/', DeliveryRequestListCreateView.as_view(), name='delivery-list-create'),
    path('request/<int:pk>/', DeliveryRequestRetrieveUpdateView.as_view(), name='delivery-retrieve-update'),
    
]

from django.urls import path
from .views import DeliveryRequestDestroyView, DeliveryRequestListCreateView, DeliveryRequestRetrieveUpdateView

urlpatterns = [
    path('request/', DeliveryRequestListCreateView.as_view(), name='delivery-list-create'),
    path('request/<int:pk>/', DeliveryRequestRetrieveUpdateView.as_view(), name='delivery-retrieve-update'),
    path('requests/delete/<int:pk>/', DeliveryRequestDestroyView.as_view(), name='delivery-request-destroy'),   
]

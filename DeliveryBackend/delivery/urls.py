from django.urls import path
from .views import CustomerDeliveryRequestsView, DeliveryRequestDestroyView, DeliveryRequestListCreateView, DeliveryRequestRetrieveUpdateView, RiderDeliveryRequestListView

urlpatterns = [
    path('request/', DeliveryRequestListCreateView.as_view(), name='delivery-list-create'),
    path('request/<int:pk>/', DeliveryRequestRetrieveUpdateView.as_view(), name='delivery-retrieve-update'),
    path('requests/delete/<int:pk>/', DeliveryRequestDestroyView.as_view(), name='delivery-request-destroy'),  
    path('rider/<int:rider_id>/delivery-requests/', RiderDeliveryRequestListView.as_view(), name='rider-delivery-requests'), 
    path('customer/<int:customer_id>/delivery-requests/', CustomerDeliveryRequestsView.as_view(), name='customer-delivery-requests'),
]

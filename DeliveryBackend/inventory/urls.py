from django.urls import path
from .views import InventoryDestroyView, InventoryListCreateView, InventoryRetrieveUpdateView

urlpatterns = [
    path('items/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('items/<int:pk>/', InventoryRetrieveUpdateView.as_view(), name='inventory-retrieve-update'),
    path('items/delete/<int:pk>/', InventoryDestroyView.as_view(), name='inventory-destroy'),
]
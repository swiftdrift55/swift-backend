from django.urls import path
from .views import InventoryListCreateView, InventoryRetrieveUpdateView

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryRetrieveUpdateView.as_view(), name='inventory-retrieve-update'),
]
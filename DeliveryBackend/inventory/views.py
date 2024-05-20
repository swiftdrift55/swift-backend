from rest_framework import generics, permissions
from .models import User, Inventory
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import InventorySerializer



class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class InventoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

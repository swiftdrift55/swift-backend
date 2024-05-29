from django.contrib import admin

from .models import DeliveryRequest

# Register your models here.
@admin.register(DeliveryRequest)
class DeliveryRequestAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'pickup_address', 'sender_location', 'receiver_name', 'receiver_mobile_number', 'payment_status', 'status')
    search_fields = ('user__username', 'receiver_name')
    list_filter = ('payment_status',)
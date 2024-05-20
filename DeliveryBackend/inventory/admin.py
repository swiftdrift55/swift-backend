from django.contrib import admin

from .models import Inventory

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'product_name', 'quantity', 'total_price', 'comment')
    search_fields = ('user__username', 'company_name', 'product_name')
    list_filter = ('company_name',)

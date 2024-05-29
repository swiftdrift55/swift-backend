from django.db import models

from authentication.models import Customer


# Create your models here.
class Inventory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
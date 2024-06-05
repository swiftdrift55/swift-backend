from django.db import models
from django.utils import timezone
from authentication.models import Customer


class DeliveryRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('denied', 'Denied'),
        ('accepted', 'Accepted'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255, default='NOT SPECIFIED')
    pickup_address = models.CharField(max_length=255)
    sender_location = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    receiver_mobile_number = models.CharField(max_length=15)
    request_date = models.DateField(default=timezone.now)
    payment_status = models.BooleanField(default=False)
    payment_value = models.FloatField(default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return f"DeliveryRequest({self.customer}, {self.status})"
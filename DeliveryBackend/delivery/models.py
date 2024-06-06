from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from decimal import Decimal
from authentication.models import Customer, Rider


class DeliveryRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('denied', 'Denied'),
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255, default='NOT SPECIFIED')
    pickup_address = models.CharField(max_length=255)
    sender_location = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    receiver_mobile_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    request_date = models.DateField(default=timezone.localdate)
    payment_status = models.BooleanField(default=False)
    payment_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    assigned_rider = models.ForeignKey(Rider, on_delete=models.SET_NULL, null=True, blank=True)

    def get_assigned_rider(self):
        return self.assigned_rider


    def __str__(self):
        return f"DeliveryRequest({self.customer}, {self.status})"
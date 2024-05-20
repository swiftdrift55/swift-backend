from django.db import models

from authentication.models import User

# Create your models here.
class DeliveryRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_address = models.CharField(max_length=255)
    sender_location = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    receiver_mobile_number = models.CharField(max_length=15)
    payment_status = models.BooleanField(default=False)
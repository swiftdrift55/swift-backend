# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DeliveryRequest

@receiver(post_save, sender=DeliveryRequest)
def notify_rider(sender, instance, created, **kwargs):
    if created or instance.status == 'accepted':  # Adjust this condition based on when you want to notify the rider
        # Assuming you have a way to get the assigned rider for this delivery request
        rider = instance.get_assigned_rider()
        if rider:
            message = f"You have been assigned to a delivery request: {instance}"
            rider.send_notification(message)

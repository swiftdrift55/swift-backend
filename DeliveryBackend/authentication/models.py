from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class User(AbstractUser):
    is_rider = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add unique related_name
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permissions'
    )

class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    license_upload = models.FileField(upload_to='licenses/')

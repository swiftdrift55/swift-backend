# Generated by Django 5.0.6 on 2024-06-06 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_rider_username'),
        ('delivery', '0006_alter_deliveryrequest_payment_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='assigned_rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.rider'),
        ),
    ]

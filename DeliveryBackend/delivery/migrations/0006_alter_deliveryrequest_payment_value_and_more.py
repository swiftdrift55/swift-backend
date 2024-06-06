# Generated by Django 5.0.6 on 2024-06-06 07:15

import django.core.validators
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_deliveryrequest_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryrequest',
            name='payment_value',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='deliveryrequest',
            name='receiver_mobile_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='deliveryrequest',
            name='request_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]
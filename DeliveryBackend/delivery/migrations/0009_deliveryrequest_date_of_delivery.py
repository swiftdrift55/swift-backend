# Generated by Django 5.0.6 on 2024-06-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_alter_deliveryrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='date_of_delivery',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_create_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='customer')
    Group.objects.get_or_create(name='rider')

class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0005_rider_first_name_rider_last_name'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
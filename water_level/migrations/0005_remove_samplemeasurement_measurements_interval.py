# Generated by Django 3.2.11 on 2022-03-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_level', '0004_auto_20220301_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplemeasurement',
            name='measurements_interval',
        ),
    ]
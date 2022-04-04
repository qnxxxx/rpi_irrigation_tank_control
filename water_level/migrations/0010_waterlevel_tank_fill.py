# Generated by Django 3.2.11 on 2022-04-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_level', '0009_auto_20220401_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterlevel',
            name='tank_fill',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=10, verbose_name='Tank Full (%)'),
        ),
    ]

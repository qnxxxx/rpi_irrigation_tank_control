# Generated by Django 3.2.11 on 2022-04-01 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_level', '0008_alter_waterlevel_volume_l'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterlevel',
            old_name='failsafe_status',
            new_name='failsafe',
        ),
        migrations.RenameField(
            model_name='waterlevel',
            old_name='status_message',
            new_name='status',
        ),
    ]

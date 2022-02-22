# Generated by Django 3.2.11 on 2022-01-30 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public_chat', '0002_alter_publicchatroom_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchatroom',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='users who are connected to chat room.', to=settings.AUTH_USER_MODEL),
        ),
    ]

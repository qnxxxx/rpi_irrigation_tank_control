# Generated by Django 3.2.11 on 2022-02-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementsInterval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Measurements Interval', max_length=255, unique=True)),
                ('interval', models.IntegerField(default=10)),
                ('measurements_interval', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name_plural': 'Measurements interval',
            },
        ),
        migrations.RenameModel(
            old_name='SampleMeasurementSettings',
            new_name='SampleMeasurement',
        ),
    ]
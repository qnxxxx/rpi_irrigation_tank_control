from django.db import models

# Create your models here.


class SonarPinoutManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = SonarPinout.objects
        return qs


class SonarPinout(models.Model):
    """
    Pinout for sonar GPIO
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Sonar Pinout')
    trigger_pin = models.IntegerField(default=23)
    echo_pin = models.IntegerField(default=24)
    failsafe_pin = models.IntegerField(default=18)

    objects = SonarPinoutManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sonar pinout'


class SampleMeasurementSettingsManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = SampleMeasurementSettings.objects
        return qs


class SampleMeasurementSettings(models.Model):
    """
    Settings for the distance measurement
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Sample Measurement Settings')
    sample_size = models.IntegerField(default=11)
    sample_wait = models.DecimalField(max_digits=5, decimal_places=1, default=0.1)
    temperature = models.IntegerField(default=20)

    measurements_interval = models.IntegerField(default=10)

    objects = SampleMeasurementSettingsManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sample measurement settings'


class TankSizeManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = TankSize.objects
        return qs


class TankSize(models.Model):
    """
    Settings for sonar GPIO
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Tank Size')
    length = models.DecimalField(max_digits=5, decimal_places=1, default=100.0)
    width = models.DecimalField(max_digits=5, decimal_places=1, default=100.0)
    depth = models.DecimalField(max_digits=5, decimal_places=1, default=100.0)

    objects = TankSizeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tank size'


class WaterLevelManager(models.Manager):  # Custom query set
    @staticmethod
    def by_timestamp():
        qs = WaterLevel.objects.order_by('-timestamp')
        return qs


class WaterLevel(models.Model):
    """
    Distance from sensor to water level, measured in cm
    """
    distance = models.DecimalField(max_digits=10, decimal_places=1, default=-1.0)
    volume_m3 = models.DecimalField(max_digits=10, decimal_places=2, default=-1.0)
    volume_l = models.DecimalField(max_digits=10, decimal_places=1, default=-1.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    failsafe_engaged = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='')

    objects = WaterLevelManager()

    def __str__(self):
        return self.distance

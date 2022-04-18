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
    trigger_pin = models.IntegerField(default=23, verbose_name='Trigger pin (GPIO Number)')
    echo_pin = models.IntegerField(default=24, verbose_name='Echo pin (GPIO Number)')
    failsafe_pin = models.IntegerField(default=18, verbose_name='Failsafe pin (GPIO Number)')

    objects = SonarPinoutManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sonar pinout'


class SampleMeasurementManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = SampleMeasurement.objects
        return qs


class SampleMeasurement(models.Model):
    """
    Settings for sample distance measurement
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Sample Measurement Settings')
    sample_size = models.IntegerField(default=11, verbose_name='Sample size (Avg of this many single measurements)')
    sample_wait = models.DecimalField(max_digits=5, decimal_places=1, default=0.1, verbose_name='Sample Wait (seconds)')
    temperature = models.IntegerField(default=20, verbose_name='Temperature (°C)')

    objects = SampleMeasurementManager()

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
    length = models.DecimalField(max_digits=5, decimal_places=1, default=100.0, verbose_name='Tank Length (cm)')
    width = models.DecimalField(max_digits=5, decimal_places=1, default=100.0, verbose_name='Tank Width (cm)')
    depth = models.DecimalField(max_digits=5, decimal_places=1, default=100.0, verbose_name='Tank Depth (cm)')

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
    water_level = models.DecimalField(max_digits=10, decimal_places=1, default=-1.0, verbose_name='To Water Level (cm)')
    volume_m3 = models.DecimalField(max_digits=10, decimal_places=2, default=-1.0, verbose_name='Water Volume (m³)')
    volume_l = models.IntegerField(default=-1, verbose_name='Water Volume (liters)')
    tank_fill = models.DecimalField(max_digits=10, decimal_places=2, default=-1.0, verbose_name='Tank Full (%)')
    timestamp = models.DateTimeField(auto_now_add=True)
    failsafe = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default='')

    objects = WaterLevelManager()

    def __str__(self):
        return f'{self.timestamp}, {self.water_level}, {self.volume_m3}, {self.volume_l}, {self.tank_fill}, ' \
               f'{self.failsafe}, {self.status}'

from django.db import models


# Create your models here.
class RelayBoardPinoutManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = RelayBoardPinout.objects
        return qs


class RelayBoardPinout(models.Model):
    """
    Pinout for the relay board GPIO
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Relay Board Pinout')
    pump_pin = models.IntegerField(default=16)
    mains_pin = models.IntegerField(default=20)
    byp_pin = models.IntegerField(default=21)

    objects = RelayBoardPinoutManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Relay board pinout'


class RelayBoardStatusManager(models.Manager):  # query set
    @staticmethod
    def query_all():
        qs = RelayBoardStatus.objects
        return qs


class RelayBoardStatus(models.Model):
    """
    Pin status for the relay board GPIO
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Relay Board Status')
    pump_pin_state = models.BooleanField(default=False)
    mains_pin_state = models.BooleanField(default=False)
    byp_pin_state = models.BooleanField(default=False)

    objects = RelayBoardStatusManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Relay board status'

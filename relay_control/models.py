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

from django.db import models


# Create your models here.
class BoardInitStatusManager(models.Manager):  # Custom query set
    @staticmethod
    def query_all():
        qs = BoardInitStatus.objects
        return qs


class BoardInitStatus(models.Model):
    """
    Saving init state in db
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='RPi GPIO Init Status')
    init_state = models.BooleanField(default=False)

    objects = BoardInitStatusManager()

    class Meta:
        verbose_name_plural = 'Board Init Status'

    def __str__(self):
        return self.title


class AutomaticModeManager(models.Manager):  # Custom query set
    @staticmethod
    def query_all():
        qs = AutomaticMode.objects
        return qs


class AutomaticMode(models.Model):
    """
    Saving working mode in db.
    """
    title = models.CharField(max_length=255, unique=True, blank=False, default='Automatic mode enabled')
    automatic_mode_enabled = models.BooleanField(default=True)

    objects = AutomaticModeManager()

    class Meta:
        verbose_name_plural = 'Automatic mode'

    def __str__(self):
        return self.title

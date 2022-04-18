import os
from decouple import config

from celery import Celery

# set the default Django settings module for the 'celery' program.
if config('DEBUG', cast=bool):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings.prod')

app = Celery('water_level')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# -namespace='CELERY' means all celery-related configuration keys
# should have a 'CELERY_' prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

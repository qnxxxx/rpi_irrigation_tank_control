"""
ASGI config for tank_src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from decouple import config

import django
from channels.routing import get_default_application

if config('DEBUG', cast=bool):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings.prod')

django.setup()

application = get_default_application()

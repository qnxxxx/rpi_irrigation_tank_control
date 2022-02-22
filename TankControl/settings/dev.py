"""
Django settings for development
"""

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = f'django-insecure{config("SECRET_KEY")}'


# Mailing settings for development only!!!
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

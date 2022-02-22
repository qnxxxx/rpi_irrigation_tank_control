"""
Django settings for production

See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
"""

from .base import *


# Security settings
SECRET_KEY = config('SECRET_KEY')

# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True


# Mailing settings for production only!!!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/
#
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]
#
# STATIC_ROOT = '/var/www/tank/static/'  # manage.py collectstatic wil put static files here
# STATIC_URL = '/static/'  # django will search for user added static files here
# TEMP = '/var/www/tank/media/temp/'
#
# # MEDIA STUFF???
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/var/www/tank/media/'  # manage.py collectstatic wil put media files here

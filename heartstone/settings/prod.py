from heartstone.settings.base import *
from os import environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = environ["SECRET_KEY"]

ALLOWED_HOSTS = [
    environ["ALLOWED_HOST"],
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'Postgres',
        'PORT': 5432,
    }
}

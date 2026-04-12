# Project modules
from settings.base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_adv',
        'USER': 'django_user',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5431',
    }
}
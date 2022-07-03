from .settings import *
# PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE':  os.environ.get('ENGINE',),
        'NAME': os.environ.get('DB_NAME',),
        'USER': os.environ.get('DB_USER',),
        'PASSWORD': os.environ.get('DB_PASSWORD',),
        'HOST': 'localhost',
        'PORT': os.environ.get('DB_PORT',),
    }
}
from .base import *
import os


SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = True
ALLOWED_HOSTS = ['*']

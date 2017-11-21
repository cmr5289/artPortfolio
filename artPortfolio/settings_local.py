"""
Local settings file

Included at the end of the main settings file
    - can override settings
    - place passwords and whatnot here
"""
from .settings import INSTALLED_APPS

DEBUG = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

INSTALLED_APPS += [
    'portfolio',
    'capstone'
]

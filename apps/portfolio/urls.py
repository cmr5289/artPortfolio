"""
URLS for portfolio
"""

from views import home
from django.conf.urls import *

urlpatterns = [
    url(r'^$', home, name='portfolio_home'),
]

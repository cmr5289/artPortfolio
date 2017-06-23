# Main views
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    """
    homepage for portfolio
    """
    responseData = {
    }
    return render(request, "base.html", responseData)

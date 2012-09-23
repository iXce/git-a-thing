"""Main views"""
from django.shortcuts import render
from django.conf import settings

import time

def home(request):
    return render(request, "home.html", {})

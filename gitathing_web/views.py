"""Main views"""
from django.shortcuts import render
from django.conf import settings
from django.contrib.messages.api import get_messages

def home(request):
    return render(request, "home.html", {})

def error(request):
    """Error view"""
    messages = get_messages(request)
    return render(request, 'error.html', {'messages': messages})

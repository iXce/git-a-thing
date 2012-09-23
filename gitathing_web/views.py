"""Main views"""
from django.shortcuts import render
from django.conf import settings
from django.contrib.messages.api import get_messages

def home(request):
    return render(request, "home.html", {})

def login_error(request):
    """Error view"""
    messages = get_messages(request)
    return render(request, 'login_error.html', {'messages': messages})

def edit_profile(request):
    return render(request, "home.html", {})

def post_design(request):
    return render(request, "home.html", {})

def manage_designs(request):
    return render(request, "home.html", {})

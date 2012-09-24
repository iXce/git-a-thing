"""Main views"""
from django.shortcuts import render
from django.conf import settings
from django.contrib.messages.api import get_messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html", {})

def login_error(request):
    """Error view"""
    messages = get_messages(request)
    return render(request, 'login_error.html', {'messages': messages})

def login_error(request):
    """Error view"""
    messages = get_messages(request)
    return render(request, 'login_error.html', {'messages': messages})

def login(request):
    next = request.GET["next"] if "next" in request.GET else ""
    return render(request, 'login.html', {'next': next})

def login_openid(request):
    next = request.GET["next"] if "next" in request.GET else ""
    return render(request, 'login_openid.html', {'next': next})

@login_required
def edit_profile(request):
    return render(request, "home.html", {})

@login_required
def post_design(request):
    return render(request, "home.html", {})

def manage_designs(request):
    return render(request, "home.html", {})

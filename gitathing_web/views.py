"""Main views"""
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

from gitathing_web.models import Profile, Media, Design, Release, Build

def home(request):
    return render(request, "home.html", {})

def view_design(request, user, design, branch = None):
    return render(request, "view_design.html", {})

@login_required
def post_design(request):
    return render(request, "post_design.html", {})

@login_required
def manage_designs(request):
    return render(request, "manage_designs.html", {})

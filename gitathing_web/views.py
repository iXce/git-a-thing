"""Main views"""
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from gitathing_web.models import Profile, Media, Design, Release, Build

import gitathing_git

def home(request):
    return render(request, "home.html", {})

def view_design(request, user, design, branch = None):
    return render(request, "view_design.html", {})

class CreateRepoForm(forms.ModelForm):
    short_name = forms.RegexField(label = _('Short repository name'), max_length = 50,
        regex = r'^[\w.-]+$',
        help_text = _("Letters, digits and ./-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "./-/_ characters.")})

    initialize = forms.BooleanField(label = _('Initialize repository'), initial = False, required = False, help_text = _('Makes an initial commit with a dummy <tt>README</tt> file to enable you to clone the repo right away.'))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(CreateRepoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs["class"] = "create-repo"
        self.fields['short_name'].widget.attrs["class"] = "create-repo"
        self.fields['license'].widget.attrs["class"] = "license-select"

    class Meta:
        model = Design
        fields = ('name', 'short_name', 'license', 'initialize')

    def clean_short_name(self):
        try:
            Design.objects.filter(user = self.request.user, short_name = self.cleaned_data['short_name'], branch = "master").get()
        except Design.DoesNotExist:
            return self.cleaned_data['short_name']
        raise forms.ValidationError('You already have a repository with such a short name.') 

@login_required
def post_design(request):
    if request.method == 'POST':
        form = CreateRepoForm(request.POST, request = request)
        if form.is_valid():
            initialize = form.cleaned_data['initialize']
            design = form.save(commit = False)
            design.user = request.user
            design.repo_path = "%s/%s" % (design.user.username, design.short_name)
            gitathing_git.create_repo(design, initialize)
            design.save()
            return redirect("gitathing_upload_design", user = request.user, design = design.short_name)
    else:
        form = CreateRepoForm(request = request)
    return render(request, "post_design.html", {"form": form})

@login_required
def upload_design(request, user, design):
    return render(request, "upload_design.html", {})

@login_required
def add_description(request, user, design):
    return render(request, "add_description.html", {})

@login_required
def publish_design(request, user, design):
    return render(request, "publish_design.html", {})

@login_required
def manage_designs(request):
    return render(request, "manage_designs.html", {})

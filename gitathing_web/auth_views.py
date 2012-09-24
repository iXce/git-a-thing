from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from social_auth.utils import setting

def username_available(request):
    if request.method == "GET":
        p = request.GET.copy()
        if p.has_key('username'):
            name = p['username']
            if User.objects.filter(username__iexact = name):
                return HttpResponse(False)
            else:
                return HttpResponse(True)
    return Http404

class UsernameForm(forms.Form):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.-]+$',
        help_text = _("30 characters or fewer. Letters, digits and "
                      "./-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "./-/_ characters.")})

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

def username_form(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
            request.session['saved_username'] = form.cleaned_data['username']
            backend = request.session[name]['backend']
            return redirect('socialauth_complete', backend=backend)
    else:
        form = UsernameForm()
    name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
    backend = request.session[name]['backend']
    details = request.session[name]['kwargs']['details']
    try:
        orig_username = details['username']
        if not orig_username: orig_username = details['email']
        if not orig_username: orig_username = details['first_name']
    except KeyError:
        pass
    return render(request, 'username_form.html', {'backend': backend, 'username': orig_username, 'form': form})

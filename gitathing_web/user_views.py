"""User views"""
from django.shortcuts import render
from django.contrib.messages.api import get_messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms

# Models
from django.contrib.auth.models import User
from gitathing_web.models import Profile, Media, Design, Release, Build


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

class ProfileForm(forms.ModelForm):
    """Profile edit form"""
    email = forms.EmailField(label=_(u"Email"), required = False)
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
        except User.DoesNotExist:
            pass

    class Meta:
        model = Profile
        fields = ('about', 'email', 'display_name', 'location')

    def clean_email(self):
        try:
            User.objects.exclude(id = self.instance.user.id).filter(email = self.cleaned_data['email']).get()
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError('This email address has been registered with an existing user.') 

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(ProfileForm, self).save(*args,**kwargs)
        return profile

@login_required
def edit_profile(request):
    success = False
    profile, created = Profile.objects.get_or_create(user = request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ProfileForm(instance = profile)
    return render(request, "edit_profile.html", {"form": form, "success": success})

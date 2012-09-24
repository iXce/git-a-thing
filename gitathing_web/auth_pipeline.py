from django.shortcuts import redirect
from django.contrib.auth.models import User

def redirect_to_usernameform(*args, **kwargs):
    saved = kwargs['request'].session.get('saved_username')
    if (not saved or User.objects.filter(username__iexact = saved)) \
       and kwargs.get('user') is None:
        return redirect('gitathing_username_form')

def username(request, *args, **kwargs):
    if kwargs.get('user'):
        username = kwargs['user'].username
    else:
        username = request.session.get('saved_username')
    return {'username': username}

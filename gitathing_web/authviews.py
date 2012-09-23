from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
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

def username_form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
    backend = request.session[name]['backend']
    details = request.session[name]['kwargs']['details']
    try:
        orig_username = details['username']
        if not orig_username: orig_username = details['email']
        if not orig_username: orig_username = details['first_name']
    except KeyError:
        pass
    return render(request, 'username_form.html', {'backend': backend, 'username': orig_username})

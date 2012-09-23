"""URLs module"""
from django.conf.urls.defaults import patterns, url

from gitathing_web.authviews import username_form
from gitathing_web.views import home

urlpatterns = patterns('',
    url(r'^username_form/$', username_form, name = 'gitathing_username_form'),
    url(r'^$', home, name = 'gitathing_home'),
)

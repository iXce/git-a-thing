"""URLs module"""
from django.conf.urls.defaults import patterns, url

from gitathing_web.views import home

urlpatterns = patterns('',
    url(r'^$', home, name = 'gitathing_home'),
)

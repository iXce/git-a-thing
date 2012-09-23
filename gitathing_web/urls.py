"""URLs module"""
from django.conf.urls.defaults import patterns, url

from gitathing_web.authviews import username_form
from gitathing_web.views import home, login_error

urlpatterns = patterns('',
    url(r'^username_form/$', username_form, name = 'gitathing_username_form'),
    url(r'^login-error/$', login_error, name = 'gitathing_login_error'),
    url(r'^$', home, name = 'gitathing_home'),
)

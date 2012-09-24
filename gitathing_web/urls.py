"""URLs module"""
from django.conf.urls.defaults import patterns, url

from gitathing_web.authviews import username_form, username_available
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^username-form/$', username_form, name = 'gitathing_username_form'),
    url(r'^username-available/$', username_available, name = 'gitathing_username_available'),
    url(r'^login-openid/$', direct_to_template, {'template': 'login_openid.html'}, name = 'gitathing_login_openid'),
    url(r'^login-error/$', 'gitathing_web.views.login_error', name = 'gitathing_login_error'),
    url(r'^edit_profile/$', 'gitathing_web.views.edit_profile', name = 'gitathing_edit_profile'),
    url(r'^post_design/$', 'gitathing_web.views.post_design', name = 'gitathing_post_design'),
    url(r'^manage_designs/$', 'gitathing_web.views.manage_designs', name = 'gitathing_manage_designs'),
    url(r'^$', 'gitathing_web.views.home', name = 'gitathing_home'),
)

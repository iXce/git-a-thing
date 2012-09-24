"""URLs module"""
from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^username-form/$', 'gitathing_web.auth_views.username_form', name = 'gitathing_username_form'),
    url(r'^username-available/$', 'gitathing_web.auth_views.username_available', name = 'gitathing_username_available'),
    url(r'^login-openid/$', 'gitathing_web.user_views.login_openid', name = 'gitathing_login_openid'),
    url(r'^login/$', 'gitathing_web.user_views.login', name = 'gitathing_login'),
    url(r'^login-error/$', 'gitathing_web.user_views.login_error', name = 'gitathing_login_error'),
    url(r'^edit-profile/$', 'gitathing_web.user_views.edit_profile', name = 'gitathing_edit_profile'),
    url(r'^view-profile/(?P<user>[\w.-]+)$', 'gitathing_web.user_views.view_profile', name = 'gitathing_view_profile'),
    url(r'^post-design/$', 'gitathing_web.views.post_design', name = 'gitathing_post_design'),
    url(r'^manage-designs/$', 'gitathing_web.views.manage_designs', name = 'gitathing_manage_designs'),
    url(r'^view-design/(?P<user>[\w.-]+)/(?P<design>[\w.-]+)$', 'gitathing_web.views.view_design', name = 'gitathing_view_design'),
    url(r'^view-design/(?P<user>[\w.-]+)/(?P<design>[\w.-]+):(?P<branch>[\w-])$', 'gitathing_web.views.view_design', name = 'gitathing_view_design'),
    url(r'^$', 'gitathing_web.views.home', name = 'gitathing_home'),
)

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'', include('gitathing_web.urls')),
    url(r'^logout$', 'django.contrib.auth.views.logout', {"template_name": 'logged_out.html'}, name = 'auth_logout'),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
  + staticfiles_urlpatterns()

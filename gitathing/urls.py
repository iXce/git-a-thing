from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gitathing.views.home', name='home'),
    # url(r'^gitathing/', include('gitathing.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
  + staticfiles_urlpatterns()

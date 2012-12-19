from django.conf.urls import patterns, include, url
from bundproject import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('bundproject.projekte.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
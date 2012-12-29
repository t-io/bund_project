from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login Page
    url(r'^login/$', 'django.contrib.auth.views.login'),

    # All Urls for the geography app
    url(r'^$', 'bundproject.projekte.views.landing', name = 'landing'),
    url(r'^add/$', 'bundproject.projekte.views.add_road', name = 'add_road'),
    url(r'^add/(?P<slug_name>[-\w]+)/$', 'bundproject.projekte.views.add_road', name = 'add_road'),
    url(r'^edit/(?P<slug_name>[-\w]+)/$', 'bundproject.projekte.views.edit_road', name = 'edit_road'),
    url(r'^detail/(?P<slug_name>[-\w]+)/$', 'bundproject.projekte.views.details', name = 'road_details'),
)
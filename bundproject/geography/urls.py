from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Login Page
    url(r'^login/$', 'django.contrib.auth.views.login'),

    # All Urls for the geography app
    url(r'^$', 'bundproject.geography.views.landing', name = 'landing'),

)
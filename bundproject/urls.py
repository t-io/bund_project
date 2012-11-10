from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#redirect all requests to the responsible apps
	#in our case it's just one app --> geography

	url(r'^', include('bundproject.geography.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

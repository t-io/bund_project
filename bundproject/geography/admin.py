from django.contrib.gis import admin
from . import models

class LocationAdmin(admin.GeoModelAdmin):

	search_fields = ['name']
	list_display = ['name','point']



admin.site.register(models.Location, LocationAdmin)

class RoadAdmin(admin.GeoModelAdmin):
	search_fields = ['name']
	list_display = ['name','line']

admin.site.register(models.Road, RoadAdmin)
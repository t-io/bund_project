from django.contrib.gis import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from . import models


class LocationAdmin(admin.GeoModelAdmin):

	search_fields = ['name']
	list_display = ['name','point']





class RoadAdmin(admin.GeoModelAdmin):
	search_fields = ['name']
	list_display = ['name','art','projekt_typ','verlauf_von','verlauf_bis','kosten','bedarf','planungsstand','nutz_kost_verh']

	default_lon = 10.283203125
	default_lat = 51.31054714
	default_zoom = 6


admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Road, RoadAdmin)


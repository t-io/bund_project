from django.contrib.gis import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models
from bundproject.projekte.models import UserProfile

from django import forms
from django.contrib.auth.forms import UserChangeForm



class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )

    



class UserProfileInline(admin.StackedInline):
    model = UserProfile


    list_display = ['username','first_name', 'last_name']
    #can_delete = False
    #search_fields = ['username', 'email']
    change_user_password_template = None
    verbose_name_plural = 'Profil'
    verbose_name = 'Profil'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    fieldsets = ((None, {'fields': ('username','email','first_name', 'last_name',),}),)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','first_name', 'last_name')}
        ),
    )



class RoadAdmin(admin.GeoModelAdmin):
	search_fields = ['name']
	list_display = ['name','art','projekt_typ','verlauf_von','verlauf_bis','kosten','bedarf','planungsstand','nutz_kost_verh']

	default_lon = 10.283203125
	default_lat = 51.31054714
	default_zoom = 6


class LocationAdmin(admin.GeoModelAdmin):
	pass

class RailsAdmin(admin.GeoModelAdmin):
	pass

class WaterwayAdmin(admin.GeoModelAdmin):
	pass



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Road, RoadAdmin)

admin.site.register(models.Rails, RailsAdmin)
admin.site.register(models.Waterway, WaterwayAdmin)








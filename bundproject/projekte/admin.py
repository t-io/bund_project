from django.contrib.gis import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models
from bundproject.projekte.models import UserProfile

from django import forms
from django.contrib.auth.forms import UserChangeForm

from django.contrib.gis.geos import Point



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
class UsersAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    fieldsets = ((None, {'fields': ('username','email','password','first_name', 'last_name',),}),)

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','first_name', 'last_name')}
        ),
    )


    def response_add(self, request, obj, post_url_continue='../%s/'):
        return super(UserAdmin, self).response_add(request, obj,
                                                   post_url_continue)




class RoadAdmin(admin.OSMGeoAdmin):
    search_fields = ['name']
    list_display = ['name','sichtbar','art','projekt_typ','verlauf_von','verlauf_bis','kosten','bedarf','planungsstand','vert_entw_ziel']


    default_zoom = 6
    pnt = Point(10.283203125, 51.31054714, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords

    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'erstellt_von':
            pass
            #kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(RoadAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    '''
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('erstellt_von',)
        return self.readonly_fields
    '''

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['erstellt_von'] = request.user
        request.GET = data
        return super(RoadAdmin, self).add_view(request, form_url="", extra_context=extra_context)


class LocationAdmin(admin.GeoModelAdmin):
    pass

class RailsAdmin(admin.GeoModelAdmin):
	pass

class WaterwayAdmin(admin.GeoModelAdmin):
	pass



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UsersAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Road, RoadAdmin)


admin.site.register(models.Rails, RailsAdmin)
admin.site.register(models.Waterway, WaterwayAdmin)








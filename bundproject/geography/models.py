# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save


from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString

from django_autoslug.fields import AutoSlugField


class UserProfile(models.Model):
    LAND = (
        ('Berlin','Berlin'),
        ('Brandenburg', 'Brandenburg'),
        ('Sachsen', 'Sachsen'),
        ('Hamburg', 'Hamburg'),
        ('Bremen',  'Bremen'),
        ('Mecklemburg Vorpommern', 'Mecklemburg Vorpommern'),
        ('Tühringen',  'Tühringen'),
        ('Bayern', 'Bayern'),
        ('Sachsen Anhalt','Sachsen Anhalt'),
        ('Saarland',  'Saarland'),
        ('Hessen',  'Hessen'),
        ('Nordrhein-Westfalen','Nordrhein-Westfalen'),
        ('Niedersachsen', 'Niedersachsen'),
        ('Schleswig Holstein', 'Schleswig Holstein'),
        ('Bayern','Bayern'),
        ('Rheinland-Pfalz','Rheinland-Pfalz'),
    )




    """ extend the Django-User """
    user = models.OneToOneField(User)

    # Some more UserDate
    bundesland = models.CharField("Umweltrisiko", max_length=2, choices=LAND)
    #textengine_password = models.CharField(max_length=200)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)









class Location(models.Model):
    name = models.CharField(max_length=255)

    # Automatically create slug based on the name field
    #slug = AutoSlugField(populate_from='name', max_length=255)

    # Automatically create a unique id for this object

    # Geo Django field to store a point
    point = models.PointField(help_text='Represented as (longitude, latitude)', srid=4326)

    # You MUST use GeoManager to make Geo Queries
    objects = models.GeoManager()

    class Meta:
        verbose_name = "Umgehungsstraße"
        verbose_name_plural = "Umgehungsstraßen"
        app_label = "Projekte"
        db_table = "geography_location"



class Road(models.Model):
    
    PLANUNSSTD = (
        ('VP', 'Vorplanung'),
        ('RV', 'Raumordnungsverfahren'),
        ('RVA', 'Raumordnungsverfahren abgeschl'),
        ('LB', 'Linienbestimmung'),
        ('LBA', 'Linienbestimmt'),
        ('PF', 'Planfeststellungsverfahren'),
        ('PFA', 'Planfestgestellt'),
    )

    RISIKO = (
        ('sg', 'sehr gering'),
        ('g', 'gering'),
        ('m', 'mittel'),
        ('h', 'hoch'),
        ('sh', 'sehr hoch'),
    )



    name = models.CharField("Name",max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=255, overwrite=True)
    art = models.CharField("Art der Fernstraße", max_length=2, choices=(('AU','Autobahn'),('BU','Bundesstraße')), blank=True, null = True)
    projekt_typ = models.CharField("Art des Projekts", max_length=1, choices=(('A','Ausbau'),('N','Neubau')), blank=True, null = True)
    verlauf_von =  models.CharField("Verlauf von",max_length=255)
    verlauf_bis =  models.CharField("Verlauf bis",max_length=255)
    kosten = models.DecimalField("Kosten in Mio Euro", max_digits=10, decimal_places=2)
    bedarf = models.CharField("Bedarf", max_length=2, choices=(('VB','vordringlicher Bedarf'),('WB','weiterer Bedarf'),('KB','kein Bedarf')), blank=True, null = True)
    planungsstand = models.CharField("Planungsstand", max_length=3, choices=PLANUNSSTD, blank=True, null = True)

    nutz_kost_verh = models.DecimalField("Nutzen/Kosten Verhältnis",max_digits=4, decimal_places=1)
    umweltrisiko = models.CharField("Umweltrisiko", max_length=2, choices=RISIKO, blank=True, null = True)
    raumw_analyse = models.IntegerField("Raumwirksamkeitsanalyse", blank=True, null = True)
    stadr_bewert = models.IntegerField("Städtebauliche Bewertung", blank=True, null = True)
    


    line = models.LineStringField(srid=4269)
    objects = models.GeoManager()

    class Meta:
        verbose_name = "Straße"
        verbose_name_plural = "Straßen"
        app_label = "Projekte"
        db_table = "geography_road"


    def getLine(self):
        return str(self.line)

    def __unicode__(self):
        return self.name














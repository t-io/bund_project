# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString
from django_autoslug.fields import AutoSlugField
from django.core.validators import MaxLengthValidator
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


class UserProfile(models.Model):
    LAND = (
        ('Berlin','Berlin'),
        ('Brandenburg', 'Brandenburg'),
        ('Sachsen', 'Sachsen'),
        ('Hamburg', 'Hamburg'),
        ('Bremen',  'Bremen'),
        ('Mecklemburg-Vorpommern', 'Mecklemburg-Vorpommern'),
        ('Thueringen',  'Thüringen'),
        ('Bayern', 'Bayern'),
        ('Sachsen-Anhalt','Sachsen-Anhalt'),
        ('Saarland',  'Saarland'),
        ('Hessen',  'Hessen'),
        ('Nordrhein-Westfalen','Nordrhein-Westfalen'),
        ('Niedersachsen', 'Niedersachsen'),
        ('Schleswig-Holstein', 'Schleswig-Holstein'),
        ('Rheinland-Pfalz','Rheinland-Pfalz'),
        ('Baden-Wuerttemberg','Baden-Württemberg'),
    )
    """ extend the Django-User """
    user = models.OneToOneField(User, unique=True)

    # Some more more UserDate
    telefon = models.CharField("Telefon",max_length=255)
    bundesland = models.CharField("Landesvertretung", max_length=23, choices=LAND)

    def __unicode__(self):
        return self.user.username


    # needed to extend django user with custom information
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            print "\n\n...is Created...\n\n"
            UserProfile.objects.get_or_create(user=instance)
    
    	post_save.connect(create_user_profile, sender=User)

    
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = UserProfile.objects.get(user=self.user)
                self.pk = p.pk
            except UserProfile.DoesNotExist:
                pass
        super(UserProfile, self).save(*args, **kwargs)

  




class Location(models.Model):
 
    class Meta:
        verbose_name = "Umgehungsstraße"
        verbose_name_plural = "Umgehungsstraßen"

    def __unicode__(self):
        return self.name


class Rails(models.Model):

    class Meta:
        verbose_name = "Schiene"
        verbose_name_plural = "Schienen"

class Waterway(models.Model):

    class Meta:
        verbose_name = "Wasserstraße"
        verbose_name_plural = "Wasserstraßen"


class Road(models.Model):
    
    PLANUNSSTD = (
        ('Vorplanung', 'Vorplanung'),
        ('Raumordnungsverfahren', 'Raumordnungsverfahren'),
        ('Raumordnungsverfahren abgeschlossen', 'Raumordnungsverfahren abgeschlossen'),
        ('Linienbestimmung', 'Linienbestimmung'),
        ('Linienbestimmt', 'Linienbestimmt'),
        ('Planfeststellungsverfahren', 'Planfeststellungsverfahren'),
        ('Planfestgestellt', 'Planfestgestellt'),
    )

    RISIKO = (
        ('sehr gering', 'sehr gering'),
        ('gering', 'gering'),
        ('mittel', 'mittel'),
        ('hoch', 'hoch'),
        ('sehr hoch', 'sehr hoch'),
    )

    LAND = (
        ('', '- Leere Auswahl -'),
        ('Berlin','Berlin'),
        ('Brandenburg', 'Brandenburg'),
        ('Sachsen', 'Sachsen'),
        ('Hamburg', 'Hamburg'),
        ('Bremen',  'Bremen'),
        ('Mecklemburg-Vorpommern', 'Mecklemburg-Vorpommern'),
        ('Thueringen',  'Thüringen'),
        ('Bayern', 'Bayern'),
        ('Sachsen-Anhalt','Sachsen-Anhalt'),
        ('Saarland',  'Saarland'),
        ('Hessen',  'Hessen'),
        ('Nordrhein-Westfalen','Nordrhein-Westfalen'),
        ('Niedersachsen', 'Niedersachsen'),
        ('Schleswig-Holstein', 'Schleswig-Holstein'),
        ('Rheinland-Pfalz','Rheinland-Pfalz'),
        ('Baden-Wuerttemberg','Baden-Württemberg'),
    )

    # Straßen Informationen
    name = models.CharField("Name", unique=True ,max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=255, overwrite=True)
    art = models.CharField("Art der Fernstraße", max_length=2, choices=(('AU','Autobahn'),('BU','Bundesstraße')), blank=True, null = True)
    projekt_typ = models.CharField("Art des Projekts", max_length=1, choices=(('A','Ausbau'),('N','Neubau')), blank=True, null = True)
    verlauf_von =  models.CharField("Verlauf von",max_length=255)
    verlauf_bis =  models.CharField("Verlauf bis",max_length=255)
    kosten = models.DecimalField("Kosten in Mio Euro", max_digits=10, decimal_places=2)
    bedarf = models.CharField("Bedarf", max_length=2, choices=(('VB','vordringlicher Bedarf'),('WB','weiterer Bedarf'),('KB','kein Bedarf')), blank=True, null = True)
    planungsstand = models.CharField("Planungsstand", max_length=40, choices=PLANUNSSTD, blank=True, null = True)
    laenge = models.DecimalField("Länge in Kilometer",max_digits=5, decimal_places=1, blank=True, null = True)

    # Geometrie
    line = models.LineStringField(srid=4269)
    objects = models.GeoManager()
    
    # Projektbewertung
    nutz_kost_verh = models.DecimalField("Nutzen/Kosten Verhältnis",max_digits=4, decimal_places=1)
    umweltrisiko = models.CharField("Umweltrisiko", max_length=12, choices=RISIKO, blank=True, null = True)
    raumw_analyse = models.IntegerField("Raumwirksamkeit", blank=True, null = True)
    stadr_bewert = models.IntegerField("Städtebauliche Bewertung", blank=True, null = True)

    #Planungsziele & BUND Position
    projekt_ziel = models.TextField("Offizielles Projektziel",blank=True, null = True, validators=[MaxLengthValidator(1200)])
    kritik = models.TextField("Kritik", blank=True, null = True, validators=[MaxLengthValidator(1200)])
    #alternativen = models.TextField("Alternativen",blank=True, null = True, validators=[MaxLengthValidator(1200)])

    bild = models.ImageField(upload_to ="photos/roads/%Y%m%d/%H%M%S/", blank = True, null=True)


    # Sichtbarkeit des Projektes
    sichtbar = models.BooleanField(default=True);

    # Zugehöriges Bundesland
    bundesland = models.CharField("Bundesland", max_length=23, choices=LAND)

    # Zugehöriger User
    erstellt_von = models.ForeignKey(User, related_name="Erstellt von")

    class Meta:
        verbose_name = "Fernstraße"
        verbose_name_plural = "Fernstraßen"

    def __unicode__(self):
        return self.name


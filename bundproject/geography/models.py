from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString

class Location(models.Model):
    name = models.CharField(max_length=255)

    # Automatically create slug based on the name field
    #slug = AutoSlugField(populate_from='name', max_length=255)

    # Automatically create a unique id for this object

    # Geo Django field to store a point
    point = models.PointField(help_text='Represented as (longitude, latitude)', srid=4326)

    # You MUST use GeoManager to make Geo Queries
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.point.x, self.point.y)


class Road(models.Model):
    name = models.CharField(max_length=255)

    line = models.LineStringField(srid=4269)
    objects = models.GeoManager()


    def getLine(self):
        return str(self.line)

    def __unicode__(self):
        return self.name

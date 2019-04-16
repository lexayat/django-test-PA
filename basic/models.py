from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.




class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    secure_radius = models.IntegerField(default=1000)


class Tusa(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.TextField()
    #geo = models.ForeignKey(Location, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True, default=None)
    lng = models.FloatField(null=True, blank=True, default=None)
    mens = models.IntegerField(default=0)
    girls = models.IntegerField(default=0)
    image = models.ImageField()

    tags = models.CharField(max_length=200)
    #tags = models.ArrayField(ArrayField(models.CharField()))





    #category = models.CharField()
    #alcohol = models.BooleanField(default=True)
    #min_age = models.IntegerField()
    #max_age = models.IntegerField()
    #date_time = models.DateTimeField()
    #creator_comment = models.CharField()
    #members = models.ManyToManyField()
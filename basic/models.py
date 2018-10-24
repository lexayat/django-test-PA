from django.db import models

# Create your models here.

class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    secure_radius = models.IntegerField(default=1000)

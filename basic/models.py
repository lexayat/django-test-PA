from django.db import models

# Create your models here.




class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    secure_radius = models.IntegerField(default=1000)


#class Tusa(models.Model):
    #category = models.CharField()
   # alcohol = models.BooleanField(default=True)
   # min_age = models.IntegerField()
   # max_age = models.IntegerField()
   # date_time = models.DateTimeField()
    #creator_comment = models.CharField()
    #members = models.ManyToManyField()
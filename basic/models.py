from datetime import datetime
#from time import timezone
#from django.utils import timezone

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.







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
    date = models.DateTimeField(default=datetime(2019, 4 , 27, 10,10,3), blank=True)
    type=models.CharField(max_length=20,default='1')
    tags = models.CharField(max_length=200)
    #tags = models.ArrayField(ArrayField(models.CharField()))

    class Meta:
        unique_together = ('name',)
        ordering = ['name']

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.description)

            #category = models.CharField()
    #alcohol = models.BooleanField(default=True)
    #min_age = models.IntegerField()
    #max_age = models.IntegerField()
    #date_time = models.DateTimeField()
    #creator_comment = models.CharField()
    #members = models.ManyToManyField()
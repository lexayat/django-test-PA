from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from basic.models import Tusa


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField(default='')
    #favorite_tusas = models.ManyToManyField(Tusa)
    avatar = models.ImageField(default='def.jpg')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

#class favoriteTusas(models.Model):
#    tusa = models.ForeignKey(Tusa,on_delete=models.CASCADE)
#    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)






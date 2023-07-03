from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.IntegerField(blank=False, null=False, default= '80290000000')
    country = models.CharField(max_length=15, blank = True, null = True)
    address1 = models.CharField(max_length=50, blank = True, null = True)
    address2 = models.CharField(max_length=50, blank = True, null = True)
    city = models.CharField(max_length=40, blank = True, null = True)
    index = models.IntegerField(blank=True, null=True)
    other = models.CharField(max_length=300, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

def upload_location(Cyclone, filename):
    return '%s/%s' %(Cyclone.id, filename)
class Cyclone(models.Model):
    cyclone_image = models.ImageField(upload_to=upload_location, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0) 

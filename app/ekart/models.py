from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

def upload_location(Album, filename):
    return '%s/%s' %(Album.id, filename)

class Food(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    food_title = models.CharField(max_length =200)
    price = models.FloatField(max_length=10)
    food_logo = models.ImageField(upload_to=upload_location, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.food_title
    def get_absolute_url(self):
        return reverse('ekart:details', kwargs={'food_id': self.pk})

# # models for song lie in particular album
# class Song(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     song_title = models.CharField(max_length = 200)
#     audio_file = models.FileField()
#     is_favourite = models.BooleanField(default= False)
#     def __str__(self):
#         return self.song_title


    
    

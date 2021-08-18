from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=True,max_length=100)
    captain = models.CharField(null=True,max_length=100)
    population = models.IntegerField(null=True)
    short_intro = models.CharField(null=True,blank=True,max_length=256)
    email = models.EmailField(null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(null=True,default=False)


    def __str__(self):
        return self.name

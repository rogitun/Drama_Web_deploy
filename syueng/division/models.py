from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Team(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(null=True,max_length=100)
    name = models.CharField(max_length=100)
    captain = models.CharField(null=True,max_length=100)
    short_intro = models.CharField(null=True,blank=True,max_length=256)
    email = models.EmailField(null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(null=True,default=False)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(Team,on_delete=CASCADE,null=True,related_name='sender')
    receiver = models.ForeignKey(Team,on_delete=CASCADE,null=True,related_name='receiver')
    send_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256,null=True)
    title = models.CharField(max_length=128,null=True)
    desc = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

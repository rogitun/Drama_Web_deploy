from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from division.models import Team

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(Team,on_delete=CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,upload_to='posts/')
    date = models.DateTimeField(auto_now=True,null=True,blank=False)
    paid = models.IntegerField(null=True,blank=False)
    desc = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

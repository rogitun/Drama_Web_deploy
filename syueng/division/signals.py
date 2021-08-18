from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Team

def createUpdate(sender,instance,created,**kwargs):
    print(kwargs,'instance',instance,'created:',created)
    if created:
        print('생성')
        user = instance
        team = Team.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            captain = user.last_name,
        )

def updateTeam(sender,instance,created,**kwargs):
    print(kwargs)
    team = instance
    user = team.user
    if created==False:
        user.first_name = team.name
        user.username = team.username
        user.email = team.email
        user.last_name = team.captain
        user.save()


post_save.connect(createUpdate,sender=User)
post_save.connect(updateTeam,sender=Team)
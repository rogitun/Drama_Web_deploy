from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Team

from django.core.mail import send_mail
from django.conf import settings

def createUpdate(sender,instance,created,**kwargs):
    print(kwargs,'instance',instance,'created:',created)
    if created:
        user = instance
        team = Team.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            captain = user.last_name,
        )

        subject = "Welcome to the Greatest Show"
        message = '삼육대학교 영어연극 홈페이지 가입을 진심으로 축하드립니다. 많은 노오오력을 통해 A+를 받을 수 있도록^^'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [team.email],
            fail_silently=False,
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
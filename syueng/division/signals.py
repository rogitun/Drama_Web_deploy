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

        subject = "연극 홈페이지 가입"
        message = '정상적으로 가입 되었습니다.'

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
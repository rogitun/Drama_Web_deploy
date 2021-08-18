from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()


    return render(request,'div_main.html',{'teams':teams})
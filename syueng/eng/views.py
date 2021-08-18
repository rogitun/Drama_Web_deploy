from django.shortcuts import render
from .models import *
# Create your views here.
def post(request):
    posts = Post.objects.all()
    return render(request,'posts.html',{'posts':posts})
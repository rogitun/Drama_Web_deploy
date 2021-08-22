from django.shortcuts import redirect, render
from .models import *
from .forms import *
from datetime import date, datetime
from .utils import paginatePost

# Create your views here.
def post(request):
    posts = Post.objects.all().order_by('-created')
    posts,page_range = paginatePost(request,posts,6)
    
    context = {'posts':posts,'page_range':page_range}

    return render(request,'posts.html',context)

def createPost(request):
    user = request.user.team
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = user
            post.save()
            return redirect('account')

    context={'form':form}
    return render(request,'create_post.html',context)

def viewPost(request,pk):
    post = Post.objects.get(id=pk)
    days = datetime.now().day - post.date.day
    reviews = post.review_set.all()
    form = CustomReviewForm()

    if request.method == 'POST':
        form = CustomReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.team
            review.linked = post
            review.save()
            return redirect('view-post',post.id)

    context = {'post':post,'days':days,'form':form,'reviews':reviews}
    return render(request,'view_post.html',context)

def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.method=='POST':
        post.delete()
        return redirect('account')

    return render(request,'delete_post.html')

def editPost(request,pk):
    post = Post.objects.get(id=pk)
    form = postForm(instance=post)
    if request.method=='POST':
        form = postForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('view-post',pk)
    context = {'form':form}

    return render(request,'edit_post.html',context)
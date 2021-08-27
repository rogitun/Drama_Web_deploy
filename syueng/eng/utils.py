from django.core import paginator
from .models import *
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q

def paginatePost(request,posts,results):
    page = request.GET.get('page',1)
    print("현재 페이지 정보:", page)
    paginator = Paginator(posts,results)

    try:
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(paginator.num_pages)

    left = (int(page))-4
    if left < 1:
        left = 1
    right = (int(page))+5
    if right > paginator.num_pages:
        right = paginator.num_pages
        print(right)
    page_range = range(left,right+1)
    

    return posts,page_range

def searchPost(request):
    search_text = ''

    if request.GET.get('text'):
        search_text = request.GET.get('text')
        print('찾는 내용 : ',search_text)

    posts = Post.objects.filter(
        Q(title__icontains=search_text)|
        Q(owner__name__icontains=search_text)
    )

    return posts,search_text
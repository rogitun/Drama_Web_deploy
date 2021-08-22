from .models import *
from django.core.paginator import Paginator,EmptyPage

def paginateTeam(request,teams,results):
    page = request.GET.get('page',1)
    paginator = Paginator(teams,results)

    try:
        teams = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        teams = paginator.page(paginator.num_pages)

    left = (int(page))-4
    if left < 1:
        left = 1
    right = (int(page))+5
    if right > paginator.num_pages:
        right = paginator.num_pages
        print(right)
    page_range = range(left,right+1)
    

    return teams,page_range
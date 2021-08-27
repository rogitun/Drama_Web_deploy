from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',loginTeam,name='login'),
    path('logout/',logOut,name='logout'),
    path('register/',registerTeam,name='register'),
    path('edit/<str:pk>/',updateTeam,name='edit'),
    path('account/',accountView,name='account'),
    path('profile/<str:pk>/',profileView,name='profile'),
    path('msg-box/',msgBox,name='msg-box'),
    path('view-send/<str:pk>/',sendView,name='view-send'),
    path('view-recv/<str:pk>/',recvView,name='view-recv'),
    path('msg-send/<str:pk>/',msgSend,name='msg-send'),
]

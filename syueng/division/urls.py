from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',loginTeam,name='login'),
    path('logout/',logOut,name='logout'),
    path('register/',registerTeam,name='register'),
    path('edit/<str:pk>',updateTeam,name='edit'),
    path('account/',accountView,name='account'),
    path('profile/<str:pk>',profileView,name='profile'),
]

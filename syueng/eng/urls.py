from django.urls import path,include
from .views import *

urlpatterns = [
   path('post/',post,name='post'),
   path('create-post/',createPost,name='create-post'),
   path('view-post/<str:pk>/',viewPost,name='view-post'),
   path('delete-post/<str:pk>/',deletePost,name='delete-post'),
   path('edit-post/<str:pk>/',editPost,name='edit-post')
]
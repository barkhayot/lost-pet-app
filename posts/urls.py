from django.urls import path
from . import views

urlpatterns = [
    path('get', views.GetPosts, name='GetPosts'),
    path('create', views.PostCreate, name='PostCreate'),
    path('detail/<int:pk>', views.PostDetail, name='PostDetail')
]
from . import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterUser, name='RegisterUser'),
    path('login', views.LoginUser, name='LoginUser'),
    path('logout', views.UserLogout, name='UserLogout'),
    path('user', views.UserPage, name='UserPage')
]
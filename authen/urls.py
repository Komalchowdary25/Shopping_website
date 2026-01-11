from django.urls import path
from .views import *

urlpatterns=[
    path('login_/',login_,name='login_'),
    path('profile/',profile,name='profile'),
    path('register/',register,name='register'),
    path('logout_/',logout_,name='logout_'),
    path('update_profile/',update_profile,name='update_profile'),
    path('reset_password/',reset_password,name='reset_password'),
    path('forget_password/',forget_password,name='forget_password'),
    path('new_password/',new_password,name='new_password')
]
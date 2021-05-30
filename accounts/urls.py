from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('setrole/', views.UserRoles, name='setRoles'),
    path('set/role', views.setUserRole, name='setUserRole')
]
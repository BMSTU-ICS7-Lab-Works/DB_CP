from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('create_excursion/', views.createExcursion, name='createSight'),
    path('create_sight/', views.createSight, name='createSight'),
]
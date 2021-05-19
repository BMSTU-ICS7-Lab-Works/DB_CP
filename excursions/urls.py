from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('create_excursion/', views.createExcursion, name='createSight'),
    path('watch_excursions/', views.watch_excursions, name='watch_excursions'),

]

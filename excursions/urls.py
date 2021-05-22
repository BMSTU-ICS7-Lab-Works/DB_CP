from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('create_excursion/basis', views.addBasisToExcursion, name='createExcursion'),
    path('create_excursion/sight_add', views.addSightToExcursion, name='addSightToExcursion'),
    path('create_excursion/schedule_add', views.addScheduleToExcursion, name='addScheduleToExcursion'),
    path('watch_excursions/', views.watch_excursions, name='watch_excursions'),

]

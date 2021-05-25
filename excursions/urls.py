from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('create_excursion/basis', views.addBasisToExcursion, name='createExcursion'),
    path('create_excursion/sight_add/<str:excursion_name>', views.addSightToExcursion, name='addSightToExcursion'),
    path('create_excursion/schedule_add/<str:excursion_name>', views.addScheduleToExcursion, name='addScheduleToExcursion'),
    path('watch_excursions/schedule_choose/<str:excursion_name>', views.chooseSchedule, name='chooseSchedule'),
    path('watch_excursions/', views.watch_excursions, name='watch_excursions'),
]

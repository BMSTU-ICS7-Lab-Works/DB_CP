from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('create_excursion/', views.createExcursion, name='createSight'),
    path('create_sight/', views.createSight, name='createSight'),
    path('create_guide/', views.createGuide, name='createGuide'),
    path('watch_excursions/', views.watch_excursions, name='watch_excursions'),
    path('test/', views.test, name='test'),

]

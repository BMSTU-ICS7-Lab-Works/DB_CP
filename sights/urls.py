from django.urls import path

from . import views

urlpatterns = [
    path('sight/<str:sight_id>', views.detail, name='sight_detail'),
    path('create_sight/', views.createSight, name='createSight'),
]
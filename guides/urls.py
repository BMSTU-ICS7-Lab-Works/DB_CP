from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:guide_fio>', views.detail, name='guide_detail'),
    path('create_guide/', views.createGuide, name='createGuide'),
]
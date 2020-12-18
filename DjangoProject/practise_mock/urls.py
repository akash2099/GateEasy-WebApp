from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:album_id>/', views.details, name='details'),

    path('<int:album_id>/result/', views.result, name='result'),
]

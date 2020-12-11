from django.urls import path, include
from MECH import views

urlpatterns = [
    path('', views.mechhome, name='mechhome'),
    path('mechcontact/', views.mechcontact, name='mechcontact'),
    path('mocktest/', views.mocktest, name='mocktest'),
    path('video-lec/', views.videolec, name='videolec'),
]
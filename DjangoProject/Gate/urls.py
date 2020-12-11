from django.contrib import admin
from django.urls import path, include
from Gate import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('course', views.course, name='course'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('UserLogin', views.UserLogin, name='UserLogin'),
    path('UserLogout', views.UserLogout, name='UserLogout'),
]
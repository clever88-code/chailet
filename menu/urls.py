from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = "menu"

urlpatterns = [

    path('', views.menu_record , name='menu'),

]
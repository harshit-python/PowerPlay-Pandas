from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', league_sphere_home, name="league-sphere-home"),
]

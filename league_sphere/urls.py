from django.contrib import admin
from django.urls import path
from .views import *
from .controllers import cricket_player as cricket_player_controller

urlpatterns = [
    path('', league_sphere_home, name="league-sphere-home"),
    path('cricket-player/', cricket_player_controller.list_cricket_players, name="list-cricket-players")
]

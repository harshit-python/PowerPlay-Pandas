from django.urls import path
from .controllers import cricket_player as cricket_player_controller

urlpatterns = [
    path('cricket-players/', cricket_player_controller.filter, name='list_cricket_players'),
    path('cricket-players/<int:pk>/', cricket_player_controller.retrieve, name='retrieve_player'),
    path('cricket-players/<int:pk>/update/', cricket_player_controller.update, name='update_player'),
]

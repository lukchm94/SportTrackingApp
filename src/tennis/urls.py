from django.urls import path

from .__tennis_config import Urls
from .views.add_player import add_player, success
from .views.find_player import all_players, find_player

urlpatterns = [
    path(Urls.none.value, add_player, name=Urls.add_player.value),
    path(Urls.success_path.value, success, name=Urls.success.value),
    path(Urls.find_player_path.value, find_player, name=Urls.find_player.value),
    path(Urls.all_path.value, all_players, name=Urls.all.value),
]

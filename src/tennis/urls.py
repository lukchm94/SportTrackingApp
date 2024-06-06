from django.urls import path

from .__tennis_config import Urls
from .views.add_player import add_player, success

urlpatterns = [
    path(Urls.none.value, add_player, name=Urls.add_player.value),
    path(Urls.success_path.value, success, name=Urls.success.value),
]

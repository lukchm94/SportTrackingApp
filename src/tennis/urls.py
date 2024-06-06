from django.urls import path

from .views.add_player import add_player, success

urlpatterns = [
    path("", add_player, name="add_player"),
    path("success/", success, name="success"),
]

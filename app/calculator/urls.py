# calculator/urls.py
from django.urls import path

from .__calc_config import Paths
from .views import add, health

urlpatterns = [
    path(Paths.add_path.value, add.add, name=Paths.add.value),
    path(Paths.health_path.value, health.health, name=Paths.health.value),
]

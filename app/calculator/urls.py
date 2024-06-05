# calculator/urls.py
from django.urls import path

from .__calc_config import Paths
from .views import calculate, health

urlpatterns = [
    path(Paths.enter_num.value, calculate.enter_numbers, name=Paths.enter_num.value),
    path(Paths.none.value, calculate.calculate, name=Paths.calc.value),
    path(Paths.health_path.value, health.health, name=Paths.health.value),
]

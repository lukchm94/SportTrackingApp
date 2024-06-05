# calculator/urls.py
from django.urls import path

from .__calc_config import Paths
from .views import calculate, health

urlpatterns = [
    path("calculator/enter_numbers/", calculate.enter_numbers, name="enter_numbers"),
    path(Paths.add_path.value, calculate.calculate, name=Paths.calc.value),
    path(Paths.health_path.value, health.health, name=Paths.health.value),
]

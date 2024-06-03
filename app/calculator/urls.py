# calculator/urls.py
from django.urls import path

from . import views
from .__calc_config import Paths

urlpatterns = [
    path(Paths.add_path.value, views.add, name=Paths.add.value),
]

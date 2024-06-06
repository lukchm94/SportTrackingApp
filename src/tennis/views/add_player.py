from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.__app_configs import HttpMethods

from ..__tennis_config import Templates
from ..forms.player import TennisPlayerForm
from ..services.add_player import Add


def add_player(req: HttpRequest) -> HttpResponse:
    form: ModelForm = (
        TennisPlayerForm(req.POST)
        if req.method == HttpMethods.POST.value
        else TennisPlayerForm()
    )
    return Add(form, req).save()


def success(req: HttpRequest) -> HttpResponse:
    return render(req, Templates.success.value)

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..__tennis_config import HttpMethods, Templates
from ..forms.player import TennisPlayerForm


def add_player(req: HttpRequest) -> HttpResponse:
    print(f"req.method is: {req.method}")
    if req.method == HttpMethods.POST.value:
        print("inside POST")
        form = TennisPlayerForm(req.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            print(form.errors)
    else:
        form = TennisPlayerForm()

    return render(req, Templates.add_player.value, {"form": form})


def success(req: HttpRequest) -> HttpResponse:
    return render(req, Templates.success.value)

from django.forms import ModelForm
from django.http import HttpRequest
from django.shortcuts import redirect, render

from app.__app_configs import HttpMethods

from ..__tennis_config import Templates, Urls


class Add:
    form: ModelForm
    req: HttpRequest

    def __init__(self, form: ModelForm, req: HttpRequest) -> None:
        self.form = form
        self.req = req

    def _err_context(self) -> dict:
        return {"err": self.form.errors}

    def _get_context(self) -> dict:
        return {"form": self.form}

    def _post(self) -> None:
        if self.form.is_valid():
            self.form.save()
            return redirect(Urls.success.value)
        else:
            return render(self.req, Templates.error.value, self._err_context())

    def _get(self) -> None:
        return render(self.req, Templates.add_player.value, self._get_context())

    def save(self) -> None:
        return (
            self._post() if self.req.method == HttpMethods.POST.value else self._get()
        )

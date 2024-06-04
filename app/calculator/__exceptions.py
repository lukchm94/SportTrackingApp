from django.http import HttpResponseBadRequest


class InvalidOperation(HttpResponseBadRequest):
    def __init__(self, content: str = "Invalid operation") -> None:
        super().__init__(content)

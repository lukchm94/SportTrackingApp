from django.http import HttpRequest, JsonResponse


def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "healthy"})

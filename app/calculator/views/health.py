from django.http import HttpRequest, JsonResponse


def health(req: HttpRequest) -> JsonResponse:
    print(req.method, req.path)
    return JsonResponse({"status": "healthy"})

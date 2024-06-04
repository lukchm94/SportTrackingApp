from django.http import HttpRequest, JsonResponse


def add(request: HttpRequest) -> JsonResponse:
    # Get the two numbers from the request
    try:
        num1 = float(request.GET.get("num1", 0))
        num2 = float(request.GET.get("num2", 0))
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)

    # Calculate the sum
    result = num1 + num2

    # Return the result as JSON
    return JsonResponse({"result": result})

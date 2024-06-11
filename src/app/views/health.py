from email.policy import default

from django.http import HttpRequest, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.serializers import CharField, Serializer

from ..__app_configs import HttpMethods


class HealthResponseSerializer(Serializer):
    status = CharField(help_text="The status of the service.", default="healthy")
    method = CharField(
        help_text="The HTTP method used for the request.", default=HttpMethods.GET.value
    )


class HeathErrorSerializer(Serializer):
    message = CharField(
        help_text="The details of the error message.", default="Server Error"
    )


@extend_schema(
    responses={
        status.HTTP_200_OK: HealthResponseSerializer,
        status.HTTP_500_INTERNAL_SERVER_ERROR: HeathErrorSerializer,
    },
    summary="The API Health Check",
    description="""The `health` function returns a JSON response with the status `healthy` along with the HTTP method
    and URL path from the request. If the app is up and running the endpoint returns `healthy` status""",
    methods=[HttpMethods.GET.value],
)
@api_view([HttpMethods.GET.value])
def health(req: HttpRequest) -> JsonResponse:
    try:
        return JsonResponse({"status": "healthy", "method": req.method})

    except Exception as err:
        return JsonResponse(
            {"Message": f"Server Error: {err}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

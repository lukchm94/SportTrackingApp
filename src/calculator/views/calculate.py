from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import Template, loader
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.serializers import CharField, IntegerField, Serializer

from app.__app_configs import HttpMethods

from ..__calc_config import MathOperation, Templates
from ..__exceptions import DivisionByZeroError, OperationError
from ..service.operations import Calculate, get_error_context


def enter_numbers(req: HttpRequest) -> HttpResponse:
    template: Template = loader.get_template(Templates.enter.value)
    context: dict = {
        "allowed_operations": [
            operation
            for operation in MathOperation.list()
            if operation is not MathOperation.none.value
        ]
    }
    return HttpResponse(template.render(context, req))


class CalculationSerializer(Serializer):
    num1 = IntegerField()
    num2 = IntegerField()
    operation = CharField()


@api_view([HttpMethods.POST.value, HttpMethods.GET.value])
@swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "num1": openapi.Schema(type=openapi.TYPE_INTEGER),
            "num2": openapi.Schema(type=openapi.TYPE_INTEGER),
            "operation": openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=["num1", "num2", "operation"],
    ),
    responses={
        200: "Success response description",
        422: "Invalid numbers or division by 0 entered",
    },
    operation_description="Endpoint to render http template to calculate math operations on the two numbers",
)
def calculate(req: HttpRequest) -> HttpResponse:
    """
    The function calculates and renders a response using a template and context data based on an HTTP
    request.

    :param req: HttpRequest
    :type req: HttpRequest
    :return: An HttpResponse object is being returned, which is the result of rendering the template
    "calculator/calculate.html" with the context data obtained from the Calculate class.
    """
    if req.method == HttpMethods.GET.value:
        return redirect("enter_numbers")
    if req.POST.__len__() == 0:
        template: Template = loader.get_template(Templates.error.value)
        context: dict = get_error_context(num1, num2, operation, "No params provided")
        return HttpResponse(template.render(context, req))

    serializer = CalculationSerializer(data=req.POST)
    if serializer.is_valid():
        num1: int = serializer.validated_data["num1"]
        num2: int = serializer.validated_data["num2"]
        operation: str = serializer.validated_data["operation"]

    try:
        template: Template = loader.get_template(Templates.calculate.value)
        context: dict = Calculate(num1, num2, operation).get_context()

    except (DivisionByZeroError, OperationError) as err:
        template: Template = loader.get_template(Templates.error.value)
        context: dict = get_error_context(num1, num2, operation, err)

    return HttpResponse(template.render(context, req))

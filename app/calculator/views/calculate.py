from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template import Template, loader

from ..__calc_config import CalcTemplates, HttpMethods, MathOperation
from ..__exceptions import DivisionByZeroError, OperationError
from ..service.operations import Calculate, get_error_context


def enter_numbers(req: HttpRequest) -> HttpResponse:
    template = loader.get_template("calculator/enter_numbers.html")
    return HttpResponse(template.render({}, req))


def calculate(req: HttpRequest) -> HttpResponse:
    """
    The function calculates and renders a response using a template and context data based on an HTTP
    request.

    :param req: HttpRequest
    :type req: HttpRequest
    :return: An HttpResponse object is being returned, which is the result of rendering the template
    "calculator/calculate.html" with the context data obtained from the Calculate class.
    """
    if req.method == HttpMethods.POST.value:
        num1 = int(req.POST.get("num1", 1))
        num2 = int(req.POST.get("num2", 1))
        operation = req.POST.get("operation", MathOperation.none.value)

        try:
            template: Template = loader.get_template(CalcTemplates.calculate.value)
            context: dict = Calculate(num1, num2, operation).get_context()

        except (DivisionByZeroError, OperationError) as err:
            template: Template = loader.get_template(CalcTemplates.error.value)
            context: dict = get_error_context(num1, num2, operation, err)

        return HttpResponse(template.render(context, req))
    return redirect("enter_numbers")

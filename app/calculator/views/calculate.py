from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.template import Template, loader

from ..__calc_config import MathOperation
from ..service.operations import Calculate


def calculate(req: HttpRequest) -> HttpResponse:
    """
    The function calculates and renders a response using a template and context data based on an HTTP
    request.

    :param req: HttpRequest
    :type req: HttpRequest
    :return: An HttpResponse object is being returned, which is the result of rendering the template
    "calculator/calculate.html" with the context data obtained from the Calculate class.
    """
    cache.clear()
    num1 = int(req.GET.get("num1", 1))
    num2 = int(req.GET.get("num2", 1))
    operation = req.GET.get("operation", MathOperation.none.value)
    template: Template = loader.get_template("calculator/calculate.html")
    context: dict = Calculate(num1, num2, operation).get_context()
    cache.clear()
    return HttpResponse(template.render(context, req))

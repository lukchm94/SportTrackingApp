from enum import Enum


class Deliminator(str, Enum):
    comma = ","
    space = " "
    dash = "-"
    vertical = "|"
    forward_slash = "/"
    none = ""
    client_ref_field = " \\| "


class ValidationEnum(Enum):
    """ValidationEnum is a custom Parent class used in specific validations / configs inside the package."""

    @classmethod
    def list(cls) -> list:
        """Returns exact list of Enum values from the class"""
        return list(map(lambda c: c.value, cls))

    @classmethod
    def to_list(cls):
        """Converts the values and always returns a list of a single objects"""
        elements = []
        for id in cls:
            elements.extend(id.value)
        return elements

    @classmethod
    def to_string(cls, separator: str = Deliminator.comma.value):
        """
        Returns Enum values as a string separated by a separator.
        Separator defaults to Deliminator.comma.value
        """
        return separator.join([str(id) for id in cls.list()])

    @classmethod
    def to_dict(cls):
        """Returns Enums as a data dictionary {Enum.element.name: Enum.element.value}"""
        return {member.name: member.value for member in cls}


class Paths(str, ValidationEnum):
    none = ""
    root = "/"
    admin = "admin"
    calc = "calculate"
    enter_num = "enter_numbers"
    enter_num_path = f"{enter_num}{root}"
    health = "health"
    health_path = f"{health}{root}"


class MathOperation(str, ValidationEnum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"
    none = ""


class HttpMethods(str, ValidationEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


class CalcTemplates(str, ValidationEnum):
    calculate = "calculator/calculate.html"
    error = "calculator/invalid_operation.html"
    enter = "calculator/enter_numbers.html"

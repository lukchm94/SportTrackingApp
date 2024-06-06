from app.__app_configs import ValidationEnum


class Paths(str, ValidationEnum):
    none = ""
    root = "/"
    admin = "admin"
    calc = "calculate"
    enter_num = "enter_numbers"
    enter_num_path = f"{enter_num}{root}"


class MathOperation(str, ValidationEnum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"
    none = ""


class Templates(str, ValidationEnum):
    calculate = "calculator/calculate.html"
    error = "calculator/invalid_operation.html"
    enter = "calculator/enter_numbers.html"

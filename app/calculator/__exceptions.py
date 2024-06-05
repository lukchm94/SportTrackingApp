from django.http import HttpResponseBadRequest

from .__calc_config import MathOperation


class InvalidOperation(HttpResponseBadRequest):
    def __init__(self, content: str = "Invalid operation") -> None:
        super().__init__(content)


class DivisionByZeroError(Exception):
    """Custom exception for division by zero with details."""

    num1: int
    num2: int

    def __init__(
        self, num1: int, num2: int, msg: str = "Cannot divide by zero."
    ) -> None:
        self.num1 = num1
        self.num2 = num2
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.msg} (num1: {self.num1}, num2: {self.num2})"


class OperationError(Exception):
    """Custom exception for division by zero."""

    operation: str
    msg: str

    def __init__(self, operation: str, msg: str = f"Invalid operation passed") -> None:
        self.operation: str = operation
        self.msg: str = msg
        super().__init__(self.msg)

    def __str__(self) -> str:
        f"{self.msg}: {self.operation} not in allowed operations: {MathOperation.list()}"

from typing import Union

from ..__calc_config import MathOperation
from ..__exceptions import InvalidOperation
from ..models.operation import OperationReq, OperationResp


class Calculate:
    req: OperationReq

    def __init__(
        self, num1: Union[int, float], num2: Union[int, float], operation: str
    ) -> None:
        self.req = OperationReq(
            num1=num1,
            num2=num2,
            operation=operation.lower(),
        )

    def _add(self) -> int:
        return self.req.num1 + self.req.num2

    def _subtract(self) -> int:
        return self.req.num1 - self.req.num2

    def _multiply(self) -> int:
        return self.req.num1 * self.req.num2

    def _divide(self) -> int:
        if self.req.num2 == 0:
            return None
        return self.req.num1 / self.req.num2

    def run(self) -> OperationResp:
        """
        This Python function performs basic math operations based on the input operation type and
        returns the result.
        :return: The `run` method is returning an `OperationResp` object. This object contains the
        numbers `num1` and `num2` from the request, the operation performed, and the result of the
        operation. If the result is `None`, it defaults to 1.
        """
        if self.req.operation == MathOperation.add.value:
            result: int = self._add()

        elif self.req.operation == MathOperation.subtract.value:
            result: int = self._subtract()

        elif self.req.operation == MathOperation.multiply.value:
            result: int = self._multiply()

        elif self.req.operation == MathOperation.divide.value:
            result: int = self._divide()

        else:
            raise InvalidOperation()

        return OperationResp(
            num1=self.req.num1,
            num2=self.req.num2,
            operation=self.req.operation,
            result=result if result is not None else 1,
        )

    def get_context(self) -> dict:
        """
        This function returns a dictionary containing the result, num1, and num2 attributes from the
        OperationResp object obtained by calling the run method.
        :return: A dictionary is being returned with keys "result", "num1", and "num2", each
        corresponding to values obtained from the operation_resp object.
        """
        operation_resp: OperationResp = self.run()
        return {
            "result": operation_resp.result,
            "num1": operation_resp.num1,
            "num2": operation_resp.num2,
            "operation": operation_resp.operation,
        }

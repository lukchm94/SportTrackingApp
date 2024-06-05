from typing import Union

from pydantic import BaseModel, Field, field_validator

from ..__calc_config import MathOperation
from ..__exceptions import OperationError


class OperationReq(BaseModel):
    num1: int = Field(default=1, description="First number for the calculator app")
    num2: int = Field(default=1, description="First number for the calculator app")
    operation: str = Field(
        default=MathOperation.add.value,
        description=f"The mathematical operation should be one of: {MathOperation.list()}",
    )

    @field_validator("operation")
    def validate_operation(cls, value):
        if value not in MathOperation.list():
            raise OperationError(value)
        return value


class OperationResp(OperationReq):
    result: Union[int, float] = Field(
        default=1, description="The result of the operation"
    )

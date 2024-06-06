import unittest
from unittest.mock import patch

from ...__calc_config import MathOperation
from ...service.operations import Calculate, DivisionByZeroError, OperationError


class TestCalculate(unittest.TestCase):

    def test_addition(self):
        calc = Calculate(2, 3, MathOperation.add.value)
        self.assertEqual(calc.run().result, 5)

    def test_subtraction(self):
        calc = Calculate(5, 3, MathOperation.subtract.value)
        self.assertEqual(calc.run().result, 2)

    def test_multiplication(self):
        calc = Calculate(2, 3, MathOperation.multiply.value)
        self.assertEqual(calc.run().result, 6)

    def test_division(self):
        calc = Calculate(6, 3, MathOperation.divide.value)
        self.assertEqual(calc.run().result, 2)

    def test_division_by_zero(self):
        calc = Calculate(6, 0, MathOperation.divide.value)
        with self.assertRaises(DivisionByZeroError):
            calc.run()

    def test_invalid_operation(self):
        with self.assertRaises(OperationError):
            calc = Calculate(2, 3, "invalid")
            calc.run()

    @patch("calculator.service.operations.Calculate._add")
    def test_addition_mocked(self, mock_add):
        mock_add.return_value = 10
        calc = Calculate(2, 3, "add")
        self.assertEqual(calc.run().result, 10)

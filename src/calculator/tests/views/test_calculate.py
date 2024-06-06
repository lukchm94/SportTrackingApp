from enum import Enum
from unittest.mock import patch

from django.test import Client, TestCase
from django.urls import reverse

from ...service.operations import DivisionByZeroError


class PatchPaths(str, Enum):
    calc = "calculator.views.calculate.Calculate"


class CalculateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.calculate_url = reverse("calculate")

    @patch(PatchPaths.calc.value)
    def test_calculate_addition(self, MockCalculate):
        # Mock the Calculate class and its get_context method
        mock_instance = MockCalculate.return_value
        mock_instance.get_context.return_value = {
            "result": 5,
            "num1": 2,
            "num2": 3,
            "operation": "add",
        }

        response = self.client.post(
            self.calculate_url, {"num1": 2, "num2": 3, "operation": "add"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "5")

    @patch(PatchPaths.calc.value)
    def test_calculate_division_by_zero(self, MockCalculate):
        mock_instance = MockCalculate.return_value
        mock_instance.get_context.side_effect = DivisionByZeroError(2, 0)

        response = self.client.post(
            self.calculate_url, {"num1": 2, "num2": 0, "operation": "divide"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Error details: Cannot divide by zero. (num1: 2, num2: 0)"
        )

    def test_redirect_for_get_request(self):
        response = self.client.get(self.calculate_url)
        self.assertRedirects(response, reverse("enter_numbers"))

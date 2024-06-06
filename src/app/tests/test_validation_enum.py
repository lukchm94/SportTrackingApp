import unittest
from enum import Enum

from ..__app_configs import ValidationEnum


class TestValidationEnum(unittest.TestCase):
    def test_list(self):
        class TestEnum(ValidationEnum):
            A = "a"
            B = "b"
            C = "c"

        self.assertEqual(TestEnum.list(), ["a", "b", "c"])

    def test_to_list(self):
        class TestEnum(ValidationEnum):
            A = ["a"]
            B = ["b"]
            C = ["c"]

        self.assertEqual(TestEnum.to_list(), ["a", "b", "c"])

    def test_to_string(self):
        class TestEnum(ValidationEnum):
            A = "a"
            B = "b"
            C = "c"

        self.assertEqual(TestEnum.to_string(), "a,b,c")

        # Testing with custom separator
        self.assertEqual(TestEnum.to_string(separator="|"), "a|b|c")

    def test_to_dict(self):
        class TestEnum(ValidationEnum):
            A = "a"
            B = "b"
            C = "c"

        self.assertEqual(TestEnum.to_dict(), {"A": "a", "B": "b", "C": "c"})

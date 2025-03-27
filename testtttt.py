import pytest
from src.app import add_numbers


class TestAppFunctions:
    """Тесты для функций приложения"""

    def test_add_numbers_positive(self):
        """Тест сложения положительных чисел"""
        assert add_numbers(2, 3) == 5
        assert add_numbers(10, 15) == 25
import pytest
from src.app import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


class TestCalculator:
    """Тесты для функций калькулятора"""

    def test_add_numbers(self):
        assert add_numbers(2, 3) == 5
        assert add_numbers(-1, 1) == 0
        assert add_numbers(0, 0) == 0

    def test_subtract_numbers(self):
        assert subtract_numbers(5, 3) == 2
        assert subtract_numbers(10, -2) == 12
        assert subtract_numbers(0, 0) == 0

    def test_multiply_numbers(self):
        assert multiply_numbers(3, 4) == 12
        assert multiply_numbers(-2, 5) == -10
        assert multiply_numbers(0, 100) == 0

    def test_divide_numbers(self):
        assert divide_numbers(10, 2) == 5
        assert divide_numbers(9, 3) == 3
        assert divide_numbers(1, 2) == 0.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_numbers(10, 0)

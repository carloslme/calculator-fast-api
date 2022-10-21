from src.calculator.calculator import multiply

import pytest


def get_test_multiply_data() -> list:
    return [(-2, 3, -6), ("1/2", "8/4", 1), (10, "5", 50)]


@pytest.mark.parametrize("num1, num2, expected", get_test_multiply_data())
def test_multiply_parametrize(num1: any, num2: any, expected: any) -> None:
    assert multiply(num1, num2) == expected

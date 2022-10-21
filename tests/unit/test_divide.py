from src.calculator.calculator import divide


import pytest


def get_test_divide_data() -> list:
    return [(10, 2, 5), ("-15/4", "1/2", -7.5), (8, "16", 0.5)]


@pytest.mark.parametrize("num1, num2, expected", get_test_divide_data())
def test_divide_parametrize(num1: any, num2: any, expected: any) -> None:
    assert divide(num1, num2) == expected

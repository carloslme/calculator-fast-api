from src.calculator.calculator import sum

import pytest


def get_test_sum_data():
    return [(0.5, 0.5, 1), (-3, -3, -6), (4, 6, 10)]


@pytest.mark.parametrize("num1, num2, expected", get_test_sum_data())
def test_suma_parametrize(num1: any, num2: any, expected: any) -> None:
    assert sum(num1, num2) == expected

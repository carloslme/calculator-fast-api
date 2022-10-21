from src.calculator.calculator import subtract

import pytest


def get_test_substract_data() -> list:
    return [(0.5, 0.5, 0), ("1/2", "1", -0.5), (10, "5", 5)]


@pytest.mark.parametrize("num1, num2, expected", get_test_substract_data())
def test_resta_parametrize(num1: any, num2: any, expected: any) -> None:
    assert subtract(num1, num2) == expected

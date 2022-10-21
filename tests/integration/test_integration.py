from src.calculator import calculator as calc

import pytest


def test_integration() -> list:
    assert (calc.sum("5", "5") * calc.subtract("5/4", "3/4")) == 5


def get_integration_test_data() -> list:
    return [(5, 5, "5/4", "3/4", 5), (8, "7/5", 15, "3/8", 137.475)]


@pytest.mark.parametrize(
    "num1, num2, num3, num4, expected", get_integration_test_data()
)
def test_integration_parametrize(
    num1: any, num2: any, num3: any, num4: any, expected: any
) -> None:
    assert (calc.sum(num1, num2) * calc.subtract(num3, num4)) == expected

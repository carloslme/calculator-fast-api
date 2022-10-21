from src.calculator.calculator import get_fractions


import pytest


def get_test_fractions_data() -> list:
    return [(10, 10), ("7/4", 1.75), (-1, -1)]


@pytest.mark.parametrize("num1, expected", get_test_fractions_data())
def test_get_fractions_parametrize(num1: any, expected: any) -> None:
    assert get_fractions(num1) == expected

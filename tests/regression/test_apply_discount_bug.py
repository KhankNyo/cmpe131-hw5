from src.pricing import *;
import pytest;

@pytest.mark.parametrize("test_input, rate, expected", [
    (10.0, 1.0, 9.9)
])
def test_apply_discount(test_input, rate, expected):
    assert apply_discount(test_input, rate) == expected;

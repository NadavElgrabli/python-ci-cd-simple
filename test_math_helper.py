# test_math_helper.py
import pytest
from math_helper import power, sqrt

# Parametrize allows running the same test with different inputs
@pytest.mark.parametrize("base,exp,expected", [
    (2, 3, 8),  # 2^3 = 8
    (3, 2, 9),  # 3^2 = 9
    (5, 0, 1),  # 5^0 = 1
])
def test_power(base, exp, expected):
    assert power(base, exp) == expected

def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    with pytest.raises(ValueError):
        sqrt(-1)  # Test square root of negative number

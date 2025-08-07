# Test cases for HumanEval/13
# Generated using Claude API



def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b:
        a, b = b, a % b
    return a


# Generated test cases:
import pytest
from math import gcd

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (10, 15, 5),
    (24, 36, 12),
    (100, 75, 25),
    (7, 11, 1),
    (-10, 15, 5),
    (10, -15, 5),
    (0, 10, 10),
    (10, 0, 10),
    (1, 1, 1),
    (2, 4, 2),
    (4, 2, 2),
    (12, 16, 4),
    (16, 12, 4),
    (21, 14, 7),
    (14, 21, 7),
])
def test_greatest_common_divisor(a, b, expected):
    assert greatest_common_divisor(a, b) == abs(expected)

def test_type_error():
    with pytest.raises(TypeError):
        greatest_common_divisor('a', 'b')

def test_value_error():
    with pytest.raises(ValueError):
        greatest_common_divisor(10.5, 15.2)
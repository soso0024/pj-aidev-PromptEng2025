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

def test_greatest_common_divisor_positive_integers():
    assert greatest_common_divisor(12, 16) == 4
    assert greatest_common_divisor(24, 36) == 12
    assert greatest_common_divisor(100, 75) == 25

def test_greatest_common_divisor_negative_integers():
    assert greatest_common_divisor(-12, 16) == 4
    assert greatest_common_divisor(-24, 36) == 12
    assert greatest_common_divisor(-100, -75) == 25

def test_greatest_common_divisor_zero():
    assert greatest_common_divisor(0, 10) == 10
    assert greatest_common_divisor(12, 0) == 12
    assert greatest_common_divisor(0, 0) == 0

@pytest.mark.parametrize("a,b,expected", [
    (12, 16, 4),
    (24, 36, 12),
    (100, 75, 25),
    (-12, 16, 4),
    (-24, 36, 12),
    (-100, -75, 25),
    (0, 10, 10),
    (12, 0, 12),
    (0, 0, 0)
])
def test_greatest_common_divisor_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected
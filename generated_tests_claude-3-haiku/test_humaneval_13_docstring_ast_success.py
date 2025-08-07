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
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(12, 16) == 4
    assert greatest_common_divisor(100, 75) == 25

def test_greatest_common_divisor_negative_integers():
    assert greatest_common_divisor(-3, 5) == 1
    assert greatest_common_divisor(25, -15) == 5
    assert greatest_common_divisor(-12, 16) == 4
    assert greatest_common_divisor(-100, 75) == 25

def test_greatest_common_divisor_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(25, 0) == 25
    assert greatest_common_divisor(0, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 1),
    (25, 15, 5),
    (12, 16, 4),
    (100, 75, 25),
    (-3, 5, 1),
    (25, -15, 5),
    (-12, 16, 4),
    (-100, 75, 25),
    (0, 5, 5),
    (25, 0, 25),
    (0, 0, 0)
])
def test_greatest_common_divisor_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
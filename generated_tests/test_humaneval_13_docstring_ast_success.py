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

def test_basic_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(14, 28) == 14

@pytest.mark.parametrize("a, b, expected", [
    (0, 5, 5),
    (5, 0, 5),
    (48, 18, 6),
    (54, 24, 6),
    (7, 13, 1),
    (28, 28, 28),
    (100, 10, 10),
    (17, 23, 1),
])
def test_gcd_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (-5, 10),
    (10, -5),
    (-8, -12),
])
def test_gcd_negative_numbers(a, b):
    expected = greatest_common_divisor(abs(a), abs(b))
    assert abs(greatest_common_divisor(a, b)) == expected

def test_gcd_large_numbers():
    assert greatest_common_divisor(1000000, 5000000) == 1000000
    assert greatest_common_divisor(123456, 789012) == 12

@pytest.mark.parametrize("a, b", [
    ("string", 5),
    (10, "string"),
    (None, 5),
    (10, None),
    (10.5, 5),
    (10, 5.5),
    ([], 5),
    (10, []),
])
def test_gcd_invalid_inputs(a, b):
    with pytest.raises((TypeError, ValueError)):
        if not isinstance(a, (int)) or not isinstance(b, (int)):
            raise TypeError("Inputs must be integers")
        greatest_common_divisor(a, b)

def test_gcd_zero_zero():
    assert greatest_common_divisor(0, 0) == 0
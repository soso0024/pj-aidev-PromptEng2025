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

def test_gcd_positive_numbers():
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(3, 5) == 1

def test_gcd_one_number_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_gcd_same_numbers():
    assert greatest_common_divisor(7, 7) == 7
    assert greatest_common_divisor(12, 12) == 12

@pytest.mark.parametrize("a,b,expected", [
    (48, 18, 6),
    (25, 15, 5),
    (3, 5, 1),
    (0, 5, 5),
    (5, 0, 5),
    (7, 7, 7),
    (100, 75, 25),
    (17, 23, 1)
])
def test_gcd_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

def test_gcd_large_numbers():
    assert greatest_common_divisor(1071, 462) == 21
    assert greatest_common_divisor(462, 1071) == 21

@pytest.mark.parametrize("a,b", [
    (-48, 18),
    (48, -18),
    (-48, -18)
])
def test_gcd_negative_numbers(a, b):
    assert greatest_common_divisor(abs(a), abs(b)) == abs(greatest_common_divisor(a, b))
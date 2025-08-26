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

def test_gcd_normal_cases():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(100, 75) == 25

def test_gcd_zero_cases():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(0, 0) == 0

def test_gcd_negative_numbers():
    assert greatest_common_divisor(-48, 18) == 6
    assert greatest_common_divisor(48, -18) == 6
    assert greatest_common_divisor(-48, -18) == 6

@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 1),
    (25, 15, 5),
    (48, 18, 6),
    (100, 75, 25),
    (0, 5, 5),
    (5, 0, 5),
    (0, 0, 0),
    (-48, 18, 6),
    (48, -18, 6),
    (-48, -18, 6)
])
def test_gcd_parametrized(a, b, expected):
    assert greatest_common_divisor(abs(a), abs(b)) == expected

def test_gcd_large_numbers():
    assert greatest_common_divisor(1071, 462) == 21
    assert greatest_common_divisor(462, 1071) == 21
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
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(100, 75) == 25

def test_gcd_one_number_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_gcd_both_zero():
    assert greatest_common_divisor(0, 0) == 0

def test_gcd_coprime_numbers():
    assert greatest_common_divisor(17, 23) == 1
    assert greatest_common_divisor(11, 13) == 1

def test_gcd_same_numbers():
    assert greatest_common_divisor(7, 7) == 7
    assert greatest_common_divisor(100, 100) == 100

@pytest.mark.parametrize("a,b,expected", [
    (48, 18, 6),
    (54, 24, 6),
    (100, 75, 25),
    (0, 5, 5),
    (5, 0, 5),
    (0, 0, 0),
    (17, 23, 1),
    (7, 7, 7)
])
def test_gcd_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

def test_gcd_negative_numbers():
    assert greatest_common_divisor(-48, 18) == 6
    assert greatest_common_divisor(48, -18) == 6
    assert greatest_common_divisor(-48, -18) == 6
    assert greatest_common_divisor(-48, -18) == 6

def greatest_common_divisor(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
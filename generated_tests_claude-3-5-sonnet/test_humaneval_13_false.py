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
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(7, 13) == 1

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (1, 1, 1),
    (100, 10, 10),
    (17, 23, 1),
    (48, 18, 6),
    (54, 24, 6),
    (128, 64, 64),
    (1071, 462, 21),
    (105, 252, 21),
])
def test_gcd_parametrized(a, b, expected):
    assert abs(greatest_common_divisor(a, b)) == expected
    assert abs(greatest_common_divisor(b, a)) == expected  # Test commutativity

def test_gcd_with_negative_numbers():
    assert abs(greatest_common_divisor(-48, 18)) == 6
    assert abs(greatest_common_divisor(48, -18)) == 6
    assert abs(greatest_common_divisor(-48, -18)) == 6

def test_gcd_with_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

@pytest.mark.parametrize("a, b", [
    ("string", 5),
    (5, "string"),
    ([], 5),
    (5, []),
    (None, 5),
    (5, None),
    ({}, 5),
    (5, {}),
    (3.14, 5),
    (5, 3.14)
])
def test_gcd_invalid_input(a, b):
    with pytest.raises(TypeError):
        greatest_common_divisor(a, b)

def test_gcd_large_numbers():
    assert greatest_common_divisor(1000000, 500000) == 500000
    assert greatest_common_divisor(123456789, 987654321) == 9

def test_gcd_prime_numbers():
    assert greatest_common_divisor(17, 23) == 1
    assert greatest_common_divisor(97, 101) == 1

def test_gcd_same_number():
    assert greatest_common_divisor(5, 5) == 5
    assert greatest_common_divisor(0, 0) == 0
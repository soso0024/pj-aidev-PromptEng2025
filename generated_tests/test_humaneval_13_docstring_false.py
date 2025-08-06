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
    (0, 0, 0),
    (1, 1, 1),
    (13, 13, 13),
    (20, 15, 5),
    (54, 24, 6),
    (48, 180, 12),
    (100, 25, 25),
    (97, 22, 1),
])
def test_gcd_parametrized(a, b, expected):
    assert greatest_common_divisor(a, b) == expected
    assert greatest_common_divisor(b, a) == expected  # Test commutativity

def test_gcd_negative_numbers():
    assert abs(greatest_common_divisor(-6, 9)) == 3
    assert abs(greatest_common_divisor(6, -9)) == 3
    assert abs(greatest_common_divisor(-6, -9)) == 3

def test_gcd_with_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_gcd_large_numbers():
    assert greatest_common_divisor(1000000, 5000000) == 1000000
    assert greatest_common_divisor(123456, 789012) == 12

@pytest.mark.parametrize("a, b", [
    ("string", 5),
    (10, "20"),
    ([], 3),
])
def test_gcd_invalid_inputs(a, b):
    with pytest.raises((TypeError, ValueError)):
        greatest_common_divisor(a, b)

def test_gcd_none_inputs():
    with pytest.raises(TypeError):
        greatest_common_divisor(None, 5)
    with pytest.raises(TypeError):
        greatest_common_divisor(5, None)
    with pytest.raises(TypeError):
        greatest_common_divisor(None, None)

def test_gcd_float_inputs():
    with pytest.raises(TypeError):
        greatest_common_divisor(3.14, 2)
    with pytest.raises(TypeError):
        greatest_common_divisor(2, 3.14)
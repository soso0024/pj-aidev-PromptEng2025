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
    assert greatest_common_divisor(a, b) == expected
    assert greatest_common_divisor(b, a) == expected

def test_gcd_with_negative_numbers():
    assert abs(greatest_common_divisor(-48, 18)) == 6
    assert abs(greatest_common_divisor(48, -18)) == 6
    assert abs(greatest_common_divisor(-48, -18)) == 6

def test_gcd_with_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_gcd_with_large_numbers():
    assert greatest_common_divisor(1000000, 500000) == 500000
    assert greatest_common_divisor(123456789, 987654321) == 9

def test_gcd_with_invalid_types():
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor("string", 10)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(10, "string")
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(1.5, 10)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(10, 1.5)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor([], 10)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(10, [])
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor({}, 10)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(10, {})

def test_gcd_with_none():
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(None, 10)
    with pytest.raises((TypeError, AttributeError)):
        greatest_common_divisor(10, None)
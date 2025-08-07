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

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b:
        a, b = b, a % b
    return abs(a)

def test_greatest_common_divisor_zero():
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(7, 0) == 7

@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 1),
    (25, 15, 5),
    (12, 16, 4),
    (100, 75, 25),
    (18, 24, 6)
])
def test_greatest_common_divisor_positive(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

def test_greatest_common_divisor_negative():
    assert greatest_common_divisor(-3, 5) == 1
    assert greatest_common_divisor(3, -5) == 1
    assert greatest_common_divisor(-25, -15) == 5

def test_greatest_common_divisor_type_error():
    with pytest.raises(TypeError):
        greatest_common_divisor("a", 5)
    with pytest.raises(TypeError):
        greatest_common_divisor(5, "b")
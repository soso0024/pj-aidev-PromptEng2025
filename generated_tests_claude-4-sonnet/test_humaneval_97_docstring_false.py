# Test cases for HumanEval/97
# Generated using Claude API


def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    return abs(a % 10) * abs(b % 10)


# Generated test cases:
import pytest

def multiply(a, b):
    return abs(a % 10) * abs(b % 10)

@pytest.mark.parametrize("a,b,expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (0, 0, 0),
    (1, 1, 1),
    (9, 9, 81),
    (10, 20, 0),
    (-10, -20, 0),
    (123, 456, 18),
    (-123, -456, 18),
    (123, -456, 18),
    (-123, 456, 18),
    (5, 0, 0),
    (0, 7, 0),
    (100, 200, 0),
    (-100, -200, 0),
    (7, 8, 56),
    (-7, -8, 56),
    (7, -8, 56),
    (-7, 8, 56),
    (999, 111, 9),
    (-999, -111, 9),
    (1000, 2000, 0),
    (1001, 2002, 2),
    (-1001, -2002, 2)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_single_digits():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == 12
    assert multiply(3, -4) == 12
    assert multiply(-3, -4) == 12

def test_multiply_with_zero_unit_digit():
    assert multiply(10, 5) == 0
    assert multiply(5, 10) == 0
    assert multiply(10, 10) == 0
    assert multiply(-10, 5) == 0
    assert multiply(5, -10) == 0
    assert multiply(-10, -10) == 0

def test_multiply_large_numbers():
    assert multiply(123456789, 987654321) == 9
    assert multiply(-123456789, 987654321) == 9
    assert multiply(123456789, -987654321) == 9
    assert multiply(-123456789, -987654321) == 9
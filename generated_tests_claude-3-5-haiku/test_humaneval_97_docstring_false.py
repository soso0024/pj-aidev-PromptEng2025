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

def test_multiply_positive_numbers():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72

def test_multiply_with_zero():
    assert multiply(2020, 1851) == 0
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(14, -15) == 20
    assert multiply(-14, 15) == 10
    assert multiply(-14, -15) == 20

def test_multiply_single_digit():
    assert multiply(7, 3) == 21
    assert multiply(9, 9) == 81

@pytest.mark.parametrize("a,b,expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (7, 3, 21),
    (9, 9, 81),
    (0, 5, 0),
    (-14, 15, 10),
    (-14, -15, 20)
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected
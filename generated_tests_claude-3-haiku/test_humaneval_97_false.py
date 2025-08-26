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
from multiply import multiply

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 0),
    (-5, 7, 35),
    (0, 0, 0),
    (3.14, 2.71, 8),
    (-10, -20, 0),
    (100, 200, 0),
    (1, 9, 9),
    (9, 1, 9),
    (10.5, 20.3, 25),
    (-5.2, 7.8, 38)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_zero():
    assert multiply(0, 0) == 0

def test_multiply_negative():
    assert multiply(-3, -4) == 12

def test_multiply_float():
    assert multiply(3.14, 2.71) == 8

def test_multiply_large_numbers():
    assert multiply(100, 200) == 0

def test_multiply_single_digit():
    assert multiply(1, 9) == 9
    assert multiply(9, 1) == 9
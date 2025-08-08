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
    (0, 0, 0),
    (1, 1, 1),
    (-1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (10, 10, 0),
    (-10, 10, 0),
    (10, -10, 0),
    (-10, -10, 0),
    (12, 34, 12),
    (-12, 34, 12),
    (12, -34, 12),
    (-12, -34, 12),
    (123, 456, 18),
    (-123, 456, 18),
    (123, -456, 18),
    (-123, -456, 18),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_zero():
    assert multiply(0, 0) == 0
    assert multiply(0, 1) == 0
    assert multiply(1, 0) == 0

def test_multiply_negative():
    assert multiply(-1, 1) == 1
    assert multiply(1, -1) == 1
    assert multiply(-1, -1) == 1

def test_multiply_large_numbers():
    assert multiply(123, 456) == 18
    assert multiply(-123, 456) == 18
    assert multiply(123, -456) == 18
    assert multiply(-123, -456) == 18

def test_multiply_edge_cases():
    assert multiply(10, 10) == 0
    assert multiply(-10, 10) == 0
    assert multiply(10, -10) == 0
    assert multiply(-10, -10) == 0
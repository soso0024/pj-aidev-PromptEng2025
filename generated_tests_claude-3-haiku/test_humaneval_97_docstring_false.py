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
from solution import multiply
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (0, 0, 0),
    (-5, 7, 35),
    (99, 99, 81),
    (1, 1, 1),
    (10, 20, 0),
    (100, 200, 0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_negative_inputs():
    assert multiply(-148, 412) == 16
    assert multiply(148, -412) == 16
    assert multiply(-19, -28) == 72

def test_zero_inputs():
    assert multiply(0, 0) == 0
    assert multiply(0, 123) == 0
    assert multiply(123, 0) == 0
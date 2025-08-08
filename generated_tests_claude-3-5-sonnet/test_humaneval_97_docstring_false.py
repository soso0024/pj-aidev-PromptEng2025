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

def test_multiply_basic():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20

@pytest.mark.parametrize("a, b, expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (0, 0, 0),
    (10, 20, 0),
    (-11, -21, 21),
    (999, 999, 81),
    (1234, 5678, 32),
    (-123, 456, 18),
    (100, 100, 0),
    (1, 1, 1),
    (-9, -9, 81),
    (42, 0, 0),
    (-10, 5, 0)
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_large_numbers():
    assert multiply(999999999, 888888888) == 72

def test_multiply_zero():
    assert multiply(0, 123) == 0
    assert multiply(123, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-1, -1) == 1
    assert multiply(-9, -9) == 81
    assert multiply(-10, -20) == 0

def test_multiply_mixed_signs():
    assert multiply(-123, 456) == 18
    assert multiply(123, -456) == 18
    assert multiply(-1, 9) == 9
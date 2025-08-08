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
    assert multiply(5, 3) == 15
    assert multiply(2, 4) == 8

def test_multiply_single_digits():
    assert multiply(7, 8) == 56
    assert multiply(1, 1) == 1

def test_multiply_with_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12
    assert multiply(-5, 3) == 15
    assert multiply(5, -3) == 15

def test_multiply_large_numbers():
    assert multiply(123, 456) == 18  # 3 * 6
    assert multiply(999, 999) == 81  # 9 * 9

@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 0),
    (15, 25, 25),
    (-15, -25, 25),
    (123, 987, 21),
    (0, 100, 0),
    (-999, 999, 81),
    (15, 27, 35),
    (-15, -27, 35)
])
def test_multiply_parametrized(a, b, expected):
    result = multiply(a, b)
    assert result == expected

def test_multiply_floating_point():
    assert multiply(3, 2) == 6
    assert multiply(-3, 2) == 6

def test_multiply_very_large_numbers():
    assert multiply(999999999, 999999999) == 81
    assert multiply(10**20, 10**20) == 0
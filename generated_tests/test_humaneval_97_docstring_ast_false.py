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

@pytest.mark.parametrize("a, b, expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (0, 0, 0),
    (-9, -9, 81),
    (10, 20, 0),
    (123, 456, 18),
    (-123, 456, 18),
    (123, -456, 18),
    (-123, -456, 18),
    (1, 1, 1),
    (9999, 9999, 81),
    (-10, 5, 0),
    (5, -10, 0),
    (42, 17, 14),
    (100, 200, 0),
    (11, 21, 1),
    (95, 95, 25),
    (1234567, 987654, 28)
])
def test_multiply(a, b, expected):
    result = multiply(a, b)
    assert result == expected, f"For inputs {a} and {b}, expected {expected} but got {result}"

def test_multiply_large_numbers():
    assert multiply(999999999, 999999999) == 81

def test_multiply_zero_with_numbers():
    assert multiply(0, 123) == 0
    assert multiply(123, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-1, -1) == 1
    assert multiply(-9, -9) == 81
    assert multiply(-10, -20) == 0
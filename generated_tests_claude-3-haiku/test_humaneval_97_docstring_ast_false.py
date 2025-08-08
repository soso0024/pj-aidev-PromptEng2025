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
from math import fabs

@pytest.mark.parametrize("a, b, expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (0, 0, 0),
    (-10, 5, 0),
    (100, 200, 0),
    (1, 1, 1),
    (99, 99, 81),
    (1000, 1, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_zero():
    assert multiply(0, 0) == 0

def test_multiply_negative():
    assert multiply(-5, 10) == 0
    assert multiply(15, -20) == 0

def test_multiply_large_numbers():
    assert multiply(12345, 67890) == 45
    assert multiply(987654321, 123456789) == 81

def test_multiply_single_digit():
    assert multiply(7, 9) == 63
    assert multiply(3, 4) == 12
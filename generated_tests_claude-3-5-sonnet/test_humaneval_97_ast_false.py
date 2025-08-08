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
    assert multiply(23, 45) == 15  # 3 * 5

def test_multiply_negative_numbers():
    assert multiply(-23, -45) == 35  # 3 * 5

def test_multiply_mixed_signs():
    assert multiply(-23, 45) == 35  # 3 * 5
    assert multiply(23, -45) == 35  # 3 * 5

def test_multiply_zero():
    assert multiply(0, 45) == 0
    assert multiply(23, 0) == 0
    assert multiply(0, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 0),  # 0 * 0
    (11, 21, 1),  # 1 * 1
    (99, 99, 81), # 9 * 9
    (-99, 99, 9), # 9 * 1
    (123, 456, 18), # 3 * 6
    (-123, -456, 28), # 3 * 6
    (1000, 2000, 0), # 0 * 0
    (-1000, -2000, 0), # 0 * 0
])
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_large_numbers():
    assert multiply(999999999, 888888888) == 72  # 9 * 8

def test_multiply_decimal_numbers():
    assert multiply(10.5, 20.7) == 35  # 5 * 7

@pytest.mark.parametrize("a, b", [
    ("string", 123),
    (123, "string"),
    (None, 123),
    (123, None),
    ({}, []),
    ([], {})
])
def test_multiply_invalid_types(a, b):
    with pytest.raises((TypeError, AttributeError)):
        multiply(a, b)
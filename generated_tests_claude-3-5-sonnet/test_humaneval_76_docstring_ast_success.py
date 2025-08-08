# Test cases for HumanEval/76
# Generated using Claude API


def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 


# Generated test cases:
import pytest

@pytest.mark.parametrize("x, n, expected", [
    (1, 4, True),
    (2, 2, True),
    (8, 2, True),
    (3, 2, False),
    (3, 1, False),
    (5, 3, False),
    (1, 1, True),
    (0, 1, False),
    (16, 2, True),
    (16, 4, True),
    (25, 5, True),
    (7, 2, False),
    (100, 10, True),
    (1000, 10, True),
    (0, 5, False),
    (1, 0, True),
    (-8, 2, False),
    (-1, 3, False),
])
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_with_large_numbers():
    assert is_simple_power(1000000, 10) == True
    assert is_simple_power(1048576, 2) == True
    assert is_simple_power(1000000001, 10) == False

@pytest.mark.parametrize("x, n", [
    ("string", 2),
    (2, "string"),
    (None, 2),
    (2, None),
    ({}, 2),
    ([], 2),
])
def test_is_simple_power_invalid_inputs(x, n):
    with pytest.raises((TypeError, ValueError)):
        is_simple_power(x, n)

def test_is_simple_power_zero_base():
    assert is_simple_power(0, 0) == False

def test_is_simple_power_negative_base():
    assert is_simple_power(4, -2) == True

def test_is_simple_power_float_inputs():
    assert is_simple_power(8.0, 2.0) == True
    assert is_simple_power(8.1, 2.0) == False
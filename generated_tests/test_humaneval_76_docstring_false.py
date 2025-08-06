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
    (16, 2, True),
    (27, 3, True),
    (25, 5, True),
    (7, 2, False),
    (10, 3, False),
    (100, 3, False),
    (0, 5, False),
    (64, 2, True),
    (81, 3, True),
    (6, 2, False),
    (15, 3, False),
    (1000000, 10, True)
])
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_negative_base():
    assert not is_simple_power(-8, 2)
    assert not is_simple_power(-27, 3)

def test_negative_power():
    assert not is_simple_power(8, -2)
    assert not is_simple_power(27, -3)

def test_zero_cases():
    assert not is_simple_power(0, 0)
    assert not is_simple_power(0, 1)
    assert not is_simple_power(0, 2)

def test_zero_exponent():
    assert is_simple_power(1, 0) == False
    assert is_simple_power(2, 0) == False
    assert is_simple_power(10, 0) == False

def test_large_numbers():
    assert is_simple_power(1000000000, 10)
    assert not is_simple_power(1000000001, 10)

def test_float_numbers():
    assert not is_simple_power(2.5, 2)
    assert not is_simple_power(3.14, 3)

@pytest.mark.parametrize("x, n", [
    ("string", 2),
    (2, "string"),
    (None, 2),
    (2, None),
    ([], 2),
    (2, [])
])
def test_invalid_input_types(x, n):
    with pytest.raises((TypeError, ValueError)):
        is_simple_power(x, n)
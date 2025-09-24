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

def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x)

def test_is_simple_power_basic_cases():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False

def test_is_simple_power_edge_cases():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(0, 1) == False
    assert is_simple_power(1, 2) == True
    assert is_simple_power(1, 100) == True

def test_is_simple_power_zero_base():
    assert is_simple_power(0, 2) == False
    assert is_simple_power(0, 5) == False
    assert is_simple_power(0, 10) == False

def test_is_simple_power_negative_numbers():
    assert is_simple_power(-1, 2) == False
    assert is_simple_power(-8, 2) == False
    assert is_simple_power(8, -2) == False
    assert is_simple_power(-1, -1) == False

def test_is_simple_power_large_numbers():
    assert is_simple_power(1024, 2) == True
    assert is_simple_power(1000, 10) == True
    assert is_simple_power(729, 3) == True
    assert is_simple_power(1023, 2) == False

@pytest.mark.parametrize("x,n,expected", [
    (1, 4, True),
    (2, 2, True),
    (4, 2, True),
    (8, 2, True),
    (16, 2, True),
    (32, 2, True),
    (3, 2, False),
    (5, 2, False),
    (6, 2, False),
    (7, 2, False),
    (9, 3, True),
    (27, 3, True),
    (81, 3, True),
    (10, 3, False),
    (28, 3, False),
    (125, 5, True),
    (124, 5, False),
    (126, 5, False)
])
def test_is_simple_power_parametrized(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_zero_exponent_equivalent():
    assert is_simple_power(1, 2) == True
    assert is_simple_power(1, 3) == True
    assert is_simple_power(1, 5) == True
    assert is_simple_power(1, 10) == True

def test_is_simple_power_first_power():
    assert is_simple_power(2, 2) == True
    assert is_simple_power(3, 3) == True
    assert is_simple_power(5, 5) == True
    assert is_simple_power(10, 10) == True

def test_is_simple_power_special_base_one():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(2, 1) == False
    assert is_simple_power(10, 1) == False
    assert is_simple_power(100, 1) == False

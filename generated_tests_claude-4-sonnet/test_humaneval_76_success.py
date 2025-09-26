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

def test_is_simple_power_basic_cases():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(1, 2) == True
    assert is_simple_power(1, 5) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(27, 3) == True
    assert is_simple_power(16, 4) == True
    assert is_simple_power(125, 5) == True

def test_is_simple_power_false_cases():
    assert is_simple_power(2, 1) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(10, 1) == False
    assert is_simple_power(6, 2) == False
    assert is_simple_power(10, 3) == False
    assert is_simple_power(15, 4) == False
    assert is_simple_power(100, 7) == False

def test_is_simple_power_edge_cases():
    assert is_simple_power(0, 2) == False
    assert is_simple_power(0, 5) == False

def test_is_simple_power_large_numbers():
    assert is_simple_power(1024, 2) == True
    assert is_simple_power(3125, 5) == True
    assert is_simple_power(1000, 10) == True
    assert is_simple_power(1023, 2) == False
    assert is_simple_power(1025, 2) == False

@pytest.mark.parametrize("x,n,expected", [
    (1, 1, True),
    (1, 2, True),
    (1, 10, True),
    (2, 1, False),
    (4, 2, True),
    (9, 3, True),
    (16, 2, True),
    (25, 5, True),
    (32, 2, True),
    (64, 4, True),
    (81, 3, True),
    (100, 10, True),
    (5, 2, False),
    (7, 3, False),
    (12, 2, False),
    (20, 4, False),
    (50, 5, False)
])
def test_is_simple_power_parametrized(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_negative_base():
    assert is_simple_power(-1, 2) == False
    assert is_simple_power(-8, 2) == False
    assert is_simple_power(-27, 3) == False
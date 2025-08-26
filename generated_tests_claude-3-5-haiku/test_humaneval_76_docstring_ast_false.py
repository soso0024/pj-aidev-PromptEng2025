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
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False

@pytest.mark.parametrize("x,n,expected", [
    (1, 1, False),
    (1, 4, True),
    (4, 2, True),
    (16, 2, True),
    (27, 3, True),
    (0, 2, False),
    (2, 3, False),
    (9, 2, False),
    (5, 5, False)
])
def test_is_simple_power_parametrized(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_edge_cases():
    assert is_simple_power(1, 1) == False
    assert is_simple_power(0, 2) == False
    assert is_simple_power(1, 0) == False

def test_is_simple_power_large_numbers():
    assert is_simple_power(1024, 2) == True
    assert is_simple_power(3125, 5) == True
    assert is_simple_power(1000000, 10) == False
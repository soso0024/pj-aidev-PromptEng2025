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
    (1, 1, True),    
    (8, 2, True),    
    (16, 2, True),   
    (27, 3, True),   
    (25, 5, True),   
    (7, 2, False),   
    (10, 2, False),  
    (100, 3, False), 
    (0, 2, False),   
    (1, 5, True),    
    (2, 1, False),   
    (1000, 10, True),
    (6561, 3, True), 
    (64, 4, True),   
    (15, 3, False)   
])
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_negative_base():
    assert not is_simple_power(-8, 2)
    assert not is_simple_power(-27, 3)

def test_is_simple_power_negative_exponent():
    assert not is_simple_power(8, -2)
    assert not is_simple_power(27, -3)

def test_is_simple_power_zero_exponent():
    assert not is_simple_power(8, 0)
    assert not is_simple_power(1, 0)

def test_is_simple_power_large_numbers():
    assert is_simple_power(1000000, 10)
    assert not is_simple_power(1000001, 10)

def test_is_simple_power_edge_cases():
    assert is_simple_power(1, 1)
    assert not is_simple_power(0, 1)
    assert not is_simple_power(1, 0)
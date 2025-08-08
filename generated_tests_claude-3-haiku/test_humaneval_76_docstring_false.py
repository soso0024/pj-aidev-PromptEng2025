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
from your_module import is_simple_power
import pytest

@pytest.mark.parametrize("x, n, expected", [
    (1, 4, True),
    (2, 2, True),
    (8, 2, True),
    (3, 2, False),
    (3, 1, False),
    (5, 3, False),
    (0, 2, False),
    (-1, 2, False),
    (4, 0, False),
    (4, 1, True),
    (16, 2, True),
    (81, 3, True),
    (1024, 2, True),
    (1, 1, True),
    (2, 1, False),
])
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_raises_error():
    with pytest.raises(TypeError):
        is_simple_power("a", 2)
    with pytest.raises(TypeError):
        is_simple_power(2, "b")
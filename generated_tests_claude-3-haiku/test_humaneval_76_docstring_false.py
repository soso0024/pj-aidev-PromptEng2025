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
    (0, 0, False),
    (-1, 2, False),
    (4, -2, False),
    (16, 2, False),
    (1.0, 1, False),
    (1, 0, False),
])
def test_is_simple_power(x, n, expected):
    assert is_simple_power(x, n) == expected

def test_is_simple_power_raises_type_error():
    with pytest.raises(TypeError):
        is_simple_power("a", 2)
    with pytest.raises(TypeError):
        is_simple_power(2, "b")
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
    (1, 2, False),
    (2, 2, True),
    (3, 2, False),
    (4, 2, True),
    (8, 2, True),
    (16, 2, True),
    (32, 2, True),
    (64, 2, True),
    (65, 2, False),
    (1, 3, False),
    (3, 3, True),
    (9, 3, True),
    (27, 3, True),
    (81, 3, True),
    (82, 3, False),
    (0, 2, False),
    (-1, 2, False),
    (1, 0, False),
    (1, -1, False),
    (0, 0, False)
])
def test_is_simple_power(x, n, expected):
    from your_module import is_simple_power
    assert is_simple_power(x, n) == expected

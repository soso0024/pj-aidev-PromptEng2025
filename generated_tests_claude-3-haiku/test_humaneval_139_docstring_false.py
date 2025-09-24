# Test cases for HumanEval/139
# Generated using Claude API


def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact


# Generated test cases:
import pytest
from math import factorial

@pytest.mark.parametrize("n,expected", [
    (4, 288),
    (1, 1),
    (0, pytest.raises(ValueError)),
    (-1, pytest.raises(ValueError)),
    (3, 6),
    ('4', pytest.raises(TypeError))
])
def test_special_factorial(n, expected):
    if isinstance(n, (float, str)):
        with expected:
            special_factorial(n)
    else:
        assert special_factorial(n) == expected

def special_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact
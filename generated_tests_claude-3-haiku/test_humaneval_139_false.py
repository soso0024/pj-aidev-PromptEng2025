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

def test_special_factorial_positive_integers():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 24
    assert special_factorial(5) == 120

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_negative_integers():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_non_integers():
    with pytest.raises(ValueError):
        special_factorial(1.5)
    with pytest.raises(ValueError):
        special_factorial("2")

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (0, 1),
])
def test_special_factorial_parametrized(input, expected):
    assert special_factorial(input) == expected

def special_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact
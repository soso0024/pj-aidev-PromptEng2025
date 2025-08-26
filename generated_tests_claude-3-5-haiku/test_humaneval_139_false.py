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

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_two():
    assert special_factorial(2) == 2

def test_special_factorial_three():
    assert special_factorial(3) == 12

def test_special_factorial_five():
    assert special_factorial(5) == 34560

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560)
])
def test_special_factorial_parametrized(n, expected):
    assert special_factorial(n) == expected

def test_special_factorial_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_large_number():
    result = special_factorial(10)
    assert result > 0
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

def special_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def test_special_factorial_basic_cases():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288

def test_special_factorial_larger_numbers():
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 24883200

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 24883200)
])
def test_special_factorial_parametrized(n, expected):
    assert special_factorial(n) == expected

def test_special_factorial_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_type_input():
    with pytest.raises(TypeError):
        special_factorial('not a number')
    with pytest.raises(TypeError):
        special_factorial([1, 2, 3])
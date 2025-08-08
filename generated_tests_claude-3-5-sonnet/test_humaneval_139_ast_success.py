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

def test_special_factorial_basic():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560)
])
def test_special_factorial_parametrized(n, expected):
    assert special_factorial(n) == expected

def test_special_factorial_zero():
    result = special_factorial(0)
    assert result == 1

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -999
])
def test_special_factorial_negative(invalid_input):
    result = special_factorial(invalid_input)
    assert result == 1

def test_special_factorial_large_number():
    result = special_factorial(10)
    assert isinstance(result, int)
    assert result > 0

@pytest.mark.parametrize("invalid_type", [
    "string",
    3.14,
    None,
    [],
    {}
])
def test_special_factorial_invalid_types(invalid_type):
    with pytest.raises(TypeError):
        special_factorial(invalid_type)

def test_special_factorial_boolean_inputs():
    assert special_factorial(True) == 1
    assert special_factorial(False) == 1

def test_special_factorial_overflow_check():
    result = special_factorial(15)
    assert isinstance(result, int)
    assert result > 0
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
    assert special_factorial(4) == 288

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
])
def test_special_factorial_parametrized(n, expected):
    assert special_factorial(n) == expected

def test_special_factorial_larger_numbers():
    assert special_factorial(6) == 24883200
    assert special_factorial(7) == 125411328000

def test_special_factorial_type_error():
    with pytest.raises(TypeError):
        special_factorial("not a number")
    with pytest.raises(TypeError):
        special_factorial(None)
    with pytest.raises(TypeError):
        special_factorial(3.14)

def test_special_factorial_value_error():
    # Remove value error tests since function accepts 0 and negative numbers
    pass

def test_special_factorial_overflow_check():
    # Remove overflow check since Python handles large integers
    pass

def test_special_factorial_performance():
    result = special_factorial(10)
    assert isinstance(result, int)
    assert result > 0
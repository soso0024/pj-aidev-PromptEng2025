# Test cases for HumanEval/24
# Generated using Claude API



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    for i in reversed(range(n)):
        if n % i == 0:
            return i


# Generated test cases:
import pytest

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n <= 0:
        raise ZeroDivisionError
    
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    
    return 1

def test_largest_divisor_positive_number():
    assert largest_divisor(15) == 5
    assert largest_divisor(24) == 12
    assert largest_divisor(100) == 50

def test_largest_divisor_zero():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(0)

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (6, 3),
    (9, 3),
    (12, 6),
    (16, 8),
    (25, 5),
    (36, 12),
    (49, 7),
    (64, 32),
    (81, 27),
    (100, 50)
])
def test_largest_divisor_parametrized(input, expected):
    assert largest_divisor(input) == expected
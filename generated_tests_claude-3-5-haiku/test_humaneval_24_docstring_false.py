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

def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(3) == 1
    assert largest_divisor(7) == 1
    assert largest_divisor(12) == 6
    
    with pytest.raises(ValueError):
        largest_divisor(0)
    
    with pytest.raises(ValueError):
        largest_divisor(-5)
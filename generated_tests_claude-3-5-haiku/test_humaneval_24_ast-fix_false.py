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
    assert largest_divisor(7) == 1
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 1
    assert largest_divisor(100) == 50

def test_largest_divisor_edge_cases():
    with pytest.raises(TypeError):
        largest_divisor(None)
    with pytest.raises(TypeError):
        largest_divisor("string")
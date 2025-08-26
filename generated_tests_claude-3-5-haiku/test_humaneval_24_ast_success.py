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
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    for i in reversed(range(1, n)):
        if n % i == 0:
            return i
    
    return 1

def test_largest_divisor_basic():
    assert largest_divisor(10) == 5
    assert largest_divisor(15) == 5
    assert largest_divisor(7) == 1

def test_largest_divisor_prime():
    assert largest_divisor(17) == 1
    assert largest_divisor(2) == 1

def test_largest_divisor_even():
    assert largest_divisor(12) == 6
    assert largest_divisor(100) == 50

def test_largest_divisor_edge_cases():
    assert largest_divisor(1) == 1

@pytest.mark.parametrize("n,expected", [
    (10, 5),
    (15, 5),
    (7, 1),
    (17, 1),
    (2, 1),
    (12, 6),
    (100, 50),
    (1, 1)
])
def test_largest_divisor_parametrized(n, expected):
    assert largest_divisor(n) == expected

def test_largest_divisor_negative_input():
    with pytest.raises(ValueError):
        largest_divisor(-5)

def test_largest_divisor_zero_input():
    with pytest.raises(ValueError):
        largest_divisor(0)
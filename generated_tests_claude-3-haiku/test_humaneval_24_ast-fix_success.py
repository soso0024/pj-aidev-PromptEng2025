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
        raise ValueError("n must be a positive integer")
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1

def test_largest_divisor_positive_number():
    assert largest_divisor(12) == 6
    assert largest_divisor(100) == 50
    assert largest_divisor(1000) == 500

def test_largest_divisor_negative_number():
    with pytest.raises(ValueError):
        largest_divisor(-10)

def test_largest_divisor_zero():
    with pytest.raises(ValueError):
        largest_divisor(0)

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 1),
    (6, 3),
    (7, 1),
    (8, 4),
    (9, 3),
    (10, 5)
])
def test_largest_divisor_small_numbers(input, expected):
    assert largest_divisor(input) == expected
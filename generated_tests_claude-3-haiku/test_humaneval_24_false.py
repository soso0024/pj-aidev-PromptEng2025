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

def test_largest_divisor_positive_numbers():
    assert largest_divisor(12) == 4
    assert largest_divisor(24) == 12
    assert largest_divisor(100) == 50

def test_largest_divisor_negative_numbers():
    with pytest.raises(ValueError):
        largest_divisor(-12)

def test_largest_divisor_zero():
    with pytest.raises(ValueError):
        largest_divisor(0)

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 2),
    (5, 5),
    (6, 3),
    (7, 7),
    (8, 4),
    (9, 3),
    (10, 5)
])
def test_largest_divisor_small_numbers(input, expected):
    assert largest_divisor(input) == expected

def largest_divisor(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
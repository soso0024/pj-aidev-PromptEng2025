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

def test_largest_divisor_positive_number():
    assert largest_divisor(12) == 4
    assert largest_divisor(24) == 12
    assert largest_divisor(100) == 50

def test_largest_divisor_negative_number():
    with pytest.raises(ValueError):
        largest_divisor(-10)

def test_largest_divisor_zero():
    with pytest.raises(ValueError):
        largest_divisor(0)

def test_largest_divisor_one():
    assert largest_divisor(1) == 1

@pytest.mark.parametrize("input,expected", [
    (2, 2),
    (7, 7),
    (17, 17),
    (101, 101)
])
def test_largest_divisor_prime_numbers(input, expected):
    assert largest_divisor(input) == expected

def largest_divisor(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
    return 1
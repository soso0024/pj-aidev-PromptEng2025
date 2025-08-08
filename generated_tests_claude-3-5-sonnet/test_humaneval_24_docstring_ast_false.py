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

def test_basic_cases():
    assert largest_divisor(15) == 5
    assert largest_divisor(28) == 14
    assert largest_divisor(100) == 50

@pytest.mark.parametrize("input_n,expected", [
    (12, 6),
    (20, 10),
    (7, 1),
    (16, 8),
    (25, 5),
    (1000, 500)
])
def test_multiple_cases(input_n, expected):
    assert largest_divisor(input_n) == expected

def test_prime_numbers():
    assert largest_divisor(2) == 1
    assert largest_divisor(3) == 1
    assert largest_divisor(17) == 1
    assert largest_divisor(23) == 1

def test_perfect_squares():
    assert largest_divisor(9) == 3
    assert largest_divisor(16) == 8
    assert largest_divisor(25) == 5
    assert largest_divisor(100) == 50

@pytest.mark.parametrize("input_n", [-1, 0])
def test_invalid_inputs(input_n):
    with pytest.raises((ValueError, ZeroDivisionError)):
        largest_divisor(input_n)

def test_large_numbers():
    assert largest_divisor(1000000) == 500000
    assert largest_divisor(999999) == 333333

def test_power_of_two():
    assert largest_divisor(2) == 1
    assert largest_divisor(4) == 2
    assert largest_divisor(8) == 4
    assert largest_divisor(16) == 8
    assert largest_divisor(32) == 16

def test_consecutive_numbers():
    assert largest_divisor(6) == 3
    assert largest_divisor(7) == 1
    assert largest_divisor(8) == 4
    assert largest_divisor(9) == 3
    assert largest_divisor(10) == 5
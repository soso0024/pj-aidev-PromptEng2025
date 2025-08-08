# Test cases for HumanEval/59
# Generated using Claude API



def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


# Generated test cases:
import pytest
from math import sqrt

def test_largest_prime_factor_basic_cases():
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(100) == 5

def test_largest_prime_factor_prime_numbers():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(97) == 97

def test_largest_prime_factor_composite_numbers():
    assert largest_prime_factor(24) == 3
    assert largest_prime_factor(84) == 7
    assert largest_prime_factor(1024) == 2

def test_largest_prime_factor_edge_cases():
    assert largest_prime_factor(4) == 2

@pytest.mark.parametrize("input,expected", [
    (13, 13),
    (15, 5),
    (21, 7),
    (100, 5),
    (2, 2),
    (17, 17),
    (24, 3),
    (84, 7),
    (1024, 2)
])
def test_largest_prime_factor_parametrized(input, expected):
    assert largest_prime_factor(input) == expected

def test_largest_prime_factor_large_number():
    assert largest_prime_factor(600851475143) > 1000

def test_largest_prime_factor_negative_input():
    with pytest.raises(ValueError):
        largest_prime_factor(-10)

def test_largest_prime_factor_zero_input():
    with pytest.raises(ValueError):
        largest_prime_factor(0)
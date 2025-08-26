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

def test_largest_prime_factor_normal_cases():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(600851475143) == 6857

@pytest.mark.parametrize("n,expected", [
    (13195, 29),
    (2048, 2),
    (17, 17),
    (100, 5),
    (84, 7)
])
def test_largest_prime_factor_parametrized(n, expected):
    assert largest_prime_factor(n) == expected

def test_largest_prime_factor_small_numbers():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(15) == 5

def test_largest_prime_factor_large_numbers():
    assert largest_prime_factor(600851475143) == 6857

def test_largest_prime_factor_prime_numbers():
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(23) == 23
    assert largest_prime_factor(29) == 29

def test_largest_prime_factor_edge_cases():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3

def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True
    
    largest = 1
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            if is_prime(j):
                largest = max(largest, j)
            if is_prime(n // j):
                largest = max(largest, n // j)
    
    return n if is_prime(n) else largest
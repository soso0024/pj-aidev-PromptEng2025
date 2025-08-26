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

def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(600851475143) == 6857
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(8) == 2

def test_largest_prime_factor_edge_cases():
    with pytest.raises(TypeError):
        largest_prime_factor(None)
    with pytest.raises(TypeError):
        largest_prime_factor("string")
    with pytest.raises(ValueError):
        largest_prime_factor(1)
    with pytest.raises(ValueError):
        largest_prime_factor(0)
    with pytest.raises(ValueError):
        largest_prime_factor(-5)
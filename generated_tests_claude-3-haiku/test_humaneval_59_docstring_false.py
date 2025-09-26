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

@pytest.mark.parametrize("n,expected", [
    (13195, 29),
    (2048, 2),
    (1, None),
    (2, 2),
    (0, None),
    (-10, None),
    (100, 5),
    (1000, 5),
    (10000, 7),
    (100000, 11),
])
def test_largest_prime_factor(n, expected):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True

    assert largest_prime_factor(n) == expected
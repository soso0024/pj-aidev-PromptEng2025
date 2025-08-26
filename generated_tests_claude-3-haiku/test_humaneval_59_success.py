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

def test_largest_prime_factor_zero():
    assert largest_prime_factor(0) == 1

def test_largest_prime_factor_negative():
    assert largest_prime_factor(-10) == 1

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 2),
    (5, 5),
    (6, 3),
    (7, 7),
    (8, 2),
    (9, 3),
    (10, 5),
    (12, 3),
    (15, 5),
    (16, 2),
    (17, 17),
    (20, 5),
    (25, 5),
    (30, 5),
    (100, 5)
])
def test_largest_prime_factor(input, expected):
    assert largest_prime_factor(input) == expected

def is_prime(k):
    if k < 2:
        return False
    for i in range(2, k - 1):
        if k % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

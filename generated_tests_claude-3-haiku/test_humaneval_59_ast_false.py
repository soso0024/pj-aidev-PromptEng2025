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

def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    if n <= 1:
        return 1
    largest = 1
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    if is_prime(n):
        largest = max(largest, n)
    return largest

def test_largest_prime_factor_zero():
    assert largest_prime_factor(0) == 1

def test_largest_prime_factor_negative():
    assert largest_prime_factor(-10) == 1

@pytest.mark.parametrize("input,expected", [
    (2, 2),
    (3, 3),
    (4, 2),
    (10, 5),
    (13, 13),
    (100, 5),
    (1000, 5),
    (1000000, 7)
])
def test_largest_prime_factor_positive(input, expected):
    assert largest_prime_factor(input) == expected

def test_largest_prime_factor_prime():
    assert largest_prime_factor(7) == 7

def test_largest_prime_factor_one():
    assert largest_prime_factor(1) == 1
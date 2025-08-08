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
        raise ValueError("Input must be greater than 1.")
    largest = 1
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    if largest == 1:
        return n
    return largest

def test_largest_prime_factor_basic():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2

def test_largest_prime_factor_negative_input():
    with pytest.raises(ValueError):
        largest_prime_factor(-10)

@pytest.mark.parametrize("input,expected", [
    (2, 2),
    (3, 3),
    (4, 2),
    (6, 3),
    (8, 2),
    (9, 3),
    (10, 5),
    (12, 3),
    (15, 5),
    (16, 2),
    (18, 3),
    (20, 5),
    (25, 5),
    (30, 5),
    (36, 3),
    (45, 5),
    (50, 5),
    (60, 5),
    (72, 3),
    (90, 5),
    (100, 5)
])
def test_largest_prime_factor_known_values(input, expected):
    assert largest_prime_factor(input) == expected

def test_largest_prime_factor_prime_input():
    with pytest.raises(ValueError):
        largest_prime_factor(7)

def test_largest_prime_factor_zero_input():
    with pytest.raises(ValueError):
        largest_prime_factor(0)
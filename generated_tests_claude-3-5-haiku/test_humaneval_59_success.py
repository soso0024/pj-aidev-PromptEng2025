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

def test_largest_prime_factor_basic_cases():
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(100) == 5
    assert largest_prime_factor(84) == 7

def test_largest_prime_factor_prime_numbers():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(29) == 29

def test_largest_prime_factor_composite_numbers():
    assert largest_prime_factor(24) == 3
    assert largest_prime_factor(56) == 7
    assert largest_prime_factor(90) == 5

def test_largest_prime_factor_edge_cases():
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(4) == 2

@pytest.mark.parametrize("n,expected", [
    (13, 13),
    (15, 5),
    (100, 5),
    (84, 7),
    (2, 2),
    (17, 17),
    (24, 3),
    (56, 7),
    (90, 5),
    (1, 1),
    (4, 2)
])
def test_largest_prime_factor_parametrized(n, expected):
    assert largest_prime_factor(n) == expected

def test_largest_prime_factor_large_number():
    assert largest_prime_factor(13195) == 29

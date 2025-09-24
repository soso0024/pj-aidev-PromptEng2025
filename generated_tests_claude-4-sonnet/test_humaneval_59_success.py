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

def largest_prime_factor(n: int):
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

def test_largest_prime_factor_small_primes():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3
    assert largest_prime_factor(5) == 5
    assert largest_prime_factor(7) == 7
    assert largest_prime_factor(11) == 11

def test_largest_prime_factor_composite_numbers():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7

def test_largest_prime_factor_larger_numbers():
    assert largest_prime_factor(30) == 5
    assert largest_prime_factor(35) == 7
    assert largest_prime_factor(42) == 7
    assert largest_prime_factor(60) == 5
    assert largest_prime_factor(77) == 11
    assert largest_prime_factor(91) == 13

def test_largest_prime_factor_edge_cases():
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1

def test_largest_prime_factor_negative_numbers():
    assert largest_prime_factor(-1) == 1
    assert largest_prime_factor(-5) == 1
    assert largest_prime_factor(-10) == 1

@pytest.mark.parametrize("n,expected", [
    (14, 7),
    (22, 11),
    (26, 13),
    (33, 11),
    (39, 13),
    (51, 17),
    (55, 11),
    (65, 13),
    (69, 23),
    (85, 17)
])
def test_largest_prime_factor_parametrized(n, expected):
    assert largest_prime_factor(n) == expected

def test_largest_prime_factor_powers_of_primes():
    assert largest_prime_factor(16) == 2
    assert largest_prime_factor(25) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(49) == 7
    assert largest_prime_factor(121) == 11

def test_largest_prime_factor_products_of_two_primes():
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(14) == 7
    assert largest_prime_factor(22) == 11
    assert largest_prime_factor(34) == 17
    assert largest_prime_factor(38) == 19

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

def test_basic_composite():
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(28) == 7

def test_large_numbers():
    assert largest_prime_factor(13195) == 29

def test_power_of_two():
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(64) == 2

def test_product_of_primes():
    assert largest_prime_factor(77) == 11
    assert largest_prime_factor(91) == 13

@pytest.mark.parametrize("input_n,expected", [
    (15, 5),
    (100, 5),
    (147, 7),
    (13195, 29),
    (2048, 2),
])
def test_multiple_cases(input_n, expected):
    assert largest_prime_factor(input_n) == expected

def test_small_numbers():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(6) == 3

def test_invalid_inputs():
    for invalid_input in [0, 1, -1, -15]:
        result = largest_prime_factor(invalid_input)
        assert result == 1

def test_square_numbers():
    assert largest_prime_factor(25) == 5
    assert largest_prime_factor(49) == 7
    assert largest_prime_factor(121) == 11

def test_consecutive_numbers():
    assert largest_prime_factor(24) == 3
    assert largest_prime_factor(30) == 5

def test_semi_prime_numbers():
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(35) == 7
    assert largest_prime_factor(51) == 17
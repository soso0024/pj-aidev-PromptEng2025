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

def test_basic_numbers():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(28) == 7
    assert largest_prime_factor(100) == 5

@pytest.mark.parametrize("input_n,expected", [
    (4, 2),
    (12, 3),
    (147, 7),
    (330, 11),
    (13195, 29)
])
def test_various_numbers(input_n, expected):
    assert largest_prime_factor(input_n) == expected

def test_small_numbers():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3

def test_perfect_squares():
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(25) == 5
    assert largest_prime_factor(49) == 7

def test_prime_numbers():
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(23) == 23
    assert largest_prime_factor(31) == 31

def test_invalid_inputs():
    for invalid_input in [0, -1, -100, -13195]:
        try:
            largest_prime_factor(invalid_input)
            pytest.fail(f"Expected ValueError for input {invalid_input}")
        except ValueError:
            pass

def test_powers_of_two():
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(16) == 2
    assert largest_prime_factor(32) == 2
    assert largest_prime_factor(64) == 2

def test_consecutive_primes():
    assert largest_prime_factor(2310) == 11
# Test cases for HumanEval/31
# Generated using Claude API



def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


# Generated test cases:
import pytest

def test_is_prime_negative_numbers():
    assert not is_prime(-1)
    assert not is_prime(-10)

def test_is_prime_zero_and_one():
    assert not is_prime(0)
    assert not is_prime(1)

@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (29, True)
])
def test_is_prime_positive_primes(input, expected):
    assert is_prime(input) == expected

@pytest.mark.parametrize("input,expected", [
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (12, False),
    (14, False),
    (15, False),
    (16, False),
    (18, False)
])
def test_is_prime_positive_non_primes(input, expected):
    assert is_prime(input) == expected

def test_is_prime_large_number():
    assert is_prime(1000000007)
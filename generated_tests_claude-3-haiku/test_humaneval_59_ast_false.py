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

def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-10) == 5
    assert largest_prime_factor(100) == 5
    assert largest_prime_factor(10000) == 97
    assert largest_prime_factor(1000000007) == 1000000007

@pytest.mark.parametrize("input,expected", [
    (13195, 29),
    (2, 2),
    (1, 1),
    (0, 1),
    (-10, 5),
    (100, 5),
    (10000, 97),
    (1000000007, 1000000007)
])
def test_largest_prime_factor_parametrized(input, expected):
    assert largest_prime_factor(input) == expected

def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False

@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (7, True),
    (10, False),
    (11, True),
    (1, False),
    (0, False),
    (-5, False)
])
def test_is_prime_parametrized(input, expected):
    assert is_prime(input) == expected
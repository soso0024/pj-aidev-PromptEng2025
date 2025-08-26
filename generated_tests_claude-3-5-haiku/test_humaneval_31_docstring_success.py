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

def test_is_prime_known_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(61) == True
    assert is_prime(101) == True
    assert is_prime(13441) == True

def test_is_prime_known_non_primes():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(15) == False

def test_is_prime_edge_cases():
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-7) == False

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (1, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (0, False),
    (-1, False)
])
def test_is_prime_parametrized(number, expected):
    assert is_prime(number) == expected

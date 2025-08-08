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

def test_is_prime_basic():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_composite():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False

def test_is_prime_edge_cases():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-1) == False
    assert is_prime(-5) == False

def test_is_prime_larger_numbers():
    assert is_prime(97) == True
    assert is_prime(100) == False
    assert is_prime(13441) == True

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (4, False),
    (61, True),
    (91, False),
    (101, True),
    (1000, False),
])
def test_is_prime_parametrized(number, expected):
    assert is_prime(number) == expected

@pytest.mark.parametrize("invalid_input", [
    "2",
    None,
    [],
    {},
])
def test_is_prime_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        is_prime(invalid_input)

def test_is_prime_known_large_primes():
    assert is_prime(7919) == True
    assert is_prime(7907) == True

def test_is_prime_known_large_composites():
    assert is_prime(7900) == False
    assert is_prime(7915) == False
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

def test_is_prime_small_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_small_non_primes():
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
    (101, True),
    (100, False),
    (0, False),
    (1, False),
    (-7, False),
    (13441, True)
])
def test_is_prime_parametrized(number, expected):
    assert is_prime(number) == expected

@pytest.mark.parametrize("non_prime", [
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 100, 1000
])
def test_non_prime_numbers(non_prime):
    assert is_prime(non_prime) == False

@pytest.mark.parametrize("prime", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
])
def test_prime_numbers(prime):
    assert is_prime(prime) == True

def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime("not a number")
    with pytest.raises(TypeError):
        is_prime([1, 2, 3])
    with pytest.raises(TypeError):
        is_prime(None)

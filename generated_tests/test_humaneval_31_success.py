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
    assert is_prime(4) == False
    assert is_prime(5) == True

@pytest.mark.parametrize("number,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (11, True),
    (13, True),
    (15, False),
    (17, True),
    (20, False),
    (23, True),
])
def test_is_prime_parametrized(number, expected):
    assert is_prime(number) == expected

def test_is_prime_negative():
    assert is_prime(-1) == False
    assert is_prime(-2) == False
    assert is_prime(-7) == False

def test_is_prime_zero():
    assert is_prime(0) == False

def test_is_prime_one():
    assert is_prime(1) == False

def test_is_prime_large_numbers():
    assert is_prime(97) == True
    assert is_prime(100) == False
    assert is_prime(999) == False

@pytest.mark.parametrize("invalid_input", [
    "2",
    None,
    [],
    {},
])
def test_is_prime_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        is_prime(invalid_input)

def test_is_prime_float():
    result = is_prime(1.5)
    assert result == False

def test_is_prime_bool():
    result = is_prime(True)
    assert result == False
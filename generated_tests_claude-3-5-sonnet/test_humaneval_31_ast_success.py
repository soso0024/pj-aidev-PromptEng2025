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

def test_is_prime_negative():
    assert not is_prime(-1)
    assert not is_prime(-10)

def test_is_prime_zero_and_one():
    assert not is_prime(0)
    assert not is_prime(1)

@pytest.mark.parametrize("number,expected", [
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
    (19, True),
    (21, False),
    (23, True),
    (25, False),
    (29, True),
    (31, True),
])
def test_is_prime_various_numbers(number, expected):
    assert is_prime(number) == expected

def test_is_prime_larger_numbers():
    assert not is_prime(100)
    assert is_prime(101)
    assert not is_prime(169)
    assert is_prime(173)

@pytest.mark.parametrize("non_integer", [
    2.5,
    3.14
])
def test_is_prime_float_inputs(non_integer):
    with pytest.raises(TypeError):
        is_prime(non_integer)

def test_is_prime_invalid_types():
    with pytest.raises(TypeError):
        is_prime("2")
    with pytest.raises(TypeError):
        is_prime([2])
    with pytest.raises(TypeError):
        is_prime(None)
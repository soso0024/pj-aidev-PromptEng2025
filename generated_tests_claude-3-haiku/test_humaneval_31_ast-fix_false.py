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
import math

@pytest.mark.parametrize("n,expected", [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (10, False),
    (11, True),
    (100, False),
    (101, True),
    (1000, False),
    (1001, True),
    (int(math.inf), False),
    ('a', TypeError),
    (None, TypeError)
])
def test_is_prime(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            is_prime(n)
    else:
        assert is_prime(n) == expected

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True
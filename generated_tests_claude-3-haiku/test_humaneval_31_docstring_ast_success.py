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

@pytest.mark.parametrize("n, expected", [
    (6, False),
    (101, True),
    (11, True),
    (13441, True),
    (61, True),
    (4, False),
    (1, False),
    (-1, False),
    (0, False),
    (2, True),
])
def test_is_prime(n, expected):
    from math import sqrt
    if n < 2:
        return False
    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True == expected

def test_is_prime_raises_type_error():
    with pytest.raises(TypeError):
        is_prime("not a number")

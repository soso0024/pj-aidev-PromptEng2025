# Test cases for HumanEval/25
# Generated using Claude API

from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact


# Generated test cases:
import pytest
import math

def test_factorize_small_numbers():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]

def test_factorize_prime_numbers():
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(17) == [17]
    assert factorize(101) == [101]

def test_factorize_large_numbers():
    assert factorize(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert factorize(360) == [2, 2, 2, 3, 3, 5]
    assert factorize(7920) == [2, 2, 2, 2, 3, 3, 5, 11]

def test_factorize_one():
    assert factorize(1) == []

@pytest.mark.parametrize("input,expected", [
    (8, [2, 2, 2]),
    (25, [5, 5]),
    (70, [2, 5, 7]),
    (1024, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    (360, [2, 2, 2, 3, 3, 5]),
    (1, []),
    (2, [2]),
    (17, [17])
])
def test_factorize_parametrized(input, expected):
    assert factorize(input) == expected

def test_factorize_negative_input():
    with pytest.raises(ValueError):
        factorize(-5)

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)
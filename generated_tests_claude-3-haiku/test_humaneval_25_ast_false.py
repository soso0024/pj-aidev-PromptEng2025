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
from typing import List
import math

def factorize(n: int) -> List[int]:
    fact = []
    i = 2
    while i <= int(math.sqrt(n)) + 1:
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact

import pytest

def test_factorize_positive_integers():
    assert factorize(1) == [1]
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(6) == [2, 3]
    assert factorize(12) == [2, 2, 3]
    assert factorize(16) == [2, 2, 2, 2]
    assert factorize(24) == [2, 2, 2, 3]
    assert factorize(30) == [2, 3, 5]
    assert factorize(100) == [2, 2, 5, 5]

def test_factorize_negative_integers():
    with pytest.raises(ValueError):
        factorize(-1)

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)

@pytest.mark.parametrize("input,expected", [
    (1, [1]),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (6, [2, 3]),
    (12, [2, 2, 3]),
    (16, [2, 2, 2, 2]),
    (24, [2, 2, 2, 3]),
    (30, [2, 3, 5]),
    (100, [2, 2, 5, 5])
])
def test_factorize_parametrized(input, expected):
    assert factorize(input) == expected
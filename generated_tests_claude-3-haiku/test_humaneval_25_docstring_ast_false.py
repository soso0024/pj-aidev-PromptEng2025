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
from typing import List

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)

def test_factorize_negative():
    with pytest.raises(ValueError):
        factorize(-5)

@pytest.mark.parametrize("input,expected", [
    (1, [1]),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (25, [5, 5]),
    (70, [2, 5, 7]),
    (100, [2, 2, 5, 5]),
    (1000, [2, 2, 2, 5, 5]),
])
def test_factorize_positive(input, expected):
    assert factorize(input) == expected

def test_factorize_prime():
    assert factorize(7) == [7]
    assert factorize(11) == [11]
    assert factorize(13) == [13]

def test_factorize_large_number():
    assert factorize(2**64 - 1) == [2**64 - 1]

def test_factorize_product():
    for n in [8, 25, 70, 100, 1000]:
        factors = factorize(n)
        assert prod(factors) == n

def prod(factors):
    result = 1
    for f in factors:
        result *= f
    return result
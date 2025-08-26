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
import pytest
import math

def factorize(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
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

def test_factorize_prime_number():
    assert factorize(17) == [17]

def test_factorize_composite_number():
    assert factorize(24) == [2, 2, 2, 3]

def test_factorize_large_number():
    assert factorize(3600) == [2, 2, 2, 2, 3, 3, 5, 5]

def test_factorize_one():
    assert factorize(1) == []

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)

def test_factorize_negative_number():
    with pytest.raises(ValueError):
        factorize(-10)

@pytest.mark.parametrize("input,expected", [
    (2, [2]),
    (4, [2, 2]),
    (100, [2, 2, 5, 5]),
    (128, [2, 2, 2, 2, 2, 2, 2]),
])
def test_factorize_multiple_cases(input, expected):
    assert factorize(input) == expected
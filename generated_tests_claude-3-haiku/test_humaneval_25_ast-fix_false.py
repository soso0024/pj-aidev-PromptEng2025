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
import pytest

def factorize(n: int) -> List[int]:
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
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

def test_factorize_positive_integers():
    assert factorize(1) == [1]
    assert factorize(2) == [2]
    assert factorize(12) == [2, 2, 3]
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(997) == [997]

def test_factorize_negative_integers():
    with pytest.raises(ValueError):
        factorize(-1)

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)

def test_factorize_large_integers():
    assert factorize(2**64 - 1) == [2**64 - 1]

def test_factorize_prime_numbers():
    assert factorize(3) == [3]
    assert factorize(7) == [7]
    assert factorize(11) == [11]
    assert factorize(13) == [13]

def test_factorize_perfect_squares():
    assert factorize(4) == [2, 2]
    assert factorize(9) == [3, 3]
    assert factorize(16) == [2, 2, 2, 2]

def test_factorize_non_integer_input():
    with pytest.raises(TypeError):
        factorize(3.14)
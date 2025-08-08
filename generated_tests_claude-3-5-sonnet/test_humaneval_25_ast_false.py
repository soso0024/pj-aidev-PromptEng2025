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
from math import sqrt
from factorize import factorize

@pytest.mark.parametrize("n,expected", [
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (12, [2, 2, 3]),
    (15, [3, 5]),
    (16, [2, 2, 2, 2]),
    (100, [2, 2, 5, 5]),
    (17, [17]),
    (23, [23]),
    (24, [2, 2, 2, 3]),
    (49, [7, 7]),
    (97, [97]),
])
def test_factorize_valid_inputs(n: int, expected: List[int]):
    assert factorize(n) == expected

@pytest.mark.parametrize("n", [
    -1,
    -12,
    -100
])
def test_factorize_invalid_inputs(n: int):
    with pytest.raises(ValueError):
        factorize(n)

def test_factorize_zero_and_one():
    assert factorize(0) == []
    assert factorize(1) == []

def test_factorize_large_number():
    assert factorize(123456789) == [3, 3, 3607, 3803]

def test_factorize_prime_number():
    assert factorize(104729) == [104729]

def test_factorize_perfect_square():
    assert factorize(144) == [2, 2, 2, 2, 3, 3]

def test_factorize_power_of_two():
    assert factorize(1024) == [2] * 10

def test_factorize_product_of_primes():
    assert factorize(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]

def test_factorize_type_error():
    with pytest.raises(TypeError):
        factorize("not a number")
    with pytest.raises(TypeError):
        factorize(3.14)
    with pytest.raises(TypeError):
        factorize(None)
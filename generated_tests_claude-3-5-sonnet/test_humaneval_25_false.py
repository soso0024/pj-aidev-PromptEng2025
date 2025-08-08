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
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (12, [2, 2, 3]),
    (100, [2, 2, 5, 5]),
    (17, [17]),
    (24, [2, 2, 2, 3]),
    (147, [3, 7, 7]),
    (13195, [5, 7, 13, 29]),
])
def test_factorize_valid_inputs(n: int, expected: List[int]):
    assert factorize(n) == expected

@pytest.mark.parametrize("n", [
    -1,
    -100,
])
def test_factorize_invalid_inputs(n: int):
    with pytest.raises(ValueError):
        factorize(n)

def test_factorize_zero():
    try:
        factorize(0)
        pytest.fail("Expected ValueError for input 0")
    except (ValueError, ZeroDivisionError):
        pass

def test_factorize_large_number():
    result = factorize(999983)  # large prime
    assert result == [999983]

def test_factorize_perfect_square():
    assert factorize(25) == [5, 5]

def test_factorize_power_of_two():
    assert factorize(32) == [2, 2, 2, 2, 2]

def test_factorize_product_of_primes():
    assert factorize(2 * 3 * 5 * 7) == [2, 3, 5, 7]

def test_factorize_type_error():
    try:
        factorize("not a number")
        pytest.fail("Expected TypeError for string input")
    except (TypeError, ValueError):
        pass
    
    try:
        factorize(3.14)
        pytest.fail("Expected TypeError for float input")
    except (TypeError, ValueError):
        pass
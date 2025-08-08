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
import math


def prod(lst):
    result = 1
    for x in lst:
        result *= x
    return result


@pytest.mark.parametrize("input_n,expected", [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (8, [2, 2, 2]),
    (12, [2, 2, 3]),
    (16, [2, 2, 2, 2]),
    (25, [5, 5]),
    (70, [2, 5, 7]),
    (100, [2, 2, 5, 5]),
    (999, [3, 3, 3, 37]),
    (997, [997]),
])
def test_factorize_valid_inputs(input_n, expected):
    from factorize import factorize
    result = factorize(input_n)
    assert result == expected
    assert prod(result) == input_n if result else 1


@pytest.mark.parametrize("input_n", [
    -1,
    -100,
    -999,
])
def test_factorize_invalid_inputs(input_n):
    with pytest.raises(ValueError):
        factorize(input_n)


def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)


@pytest.mark.parametrize("input_n", [
    1.5,
    "string",
    None,
    [],
    {},
])
def test_factorize_invalid_types(input_n):
    with pytest.raises(TypeError):
        factorize(input_n)


def test_factorize_large_number():
    result = factorize(123456789)
    assert prod(result) == 123456789


def test_factorize_prime_number():
    prime = 104729
    result = factorize(prime)
    assert result == [prime]
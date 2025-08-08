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


@pytest.mark.parametrize("n,expected", [
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
    (97, [97]),
])
def test_factorize_valid_inputs(n: int, expected: List[int], factorize):
    assert factorize(n) == expected


def test_factorize_product_equals_input(factorize):
    test_numbers = [8, 12, 15, 25, 70, 100, 999]
    for n in test_numbers:
        factors = factorize(n)
        product = 1
        for factor in factors:
            product *= factor
        assert product == n


def test_factorize_factors_are_prime(factorize):
    test_numbers = [8, 12, 15, 25, 70, 100, 999]
    for n in test_numbers:
        factors = factorize(n)
        for factor in factors:
            if factor > 1:
                is_prime = True
                for i in range(2, int(factor ** 0.5) + 1):
                    if factor % i == 0:
                        is_prime = False
                        break
                assert is_prime


def test_factorize_sorted(factorize):
    test_numbers = [8, 12, 15, 25, 70, 100, 999]
    for n in test_numbers:
        factors = factorize(n)
        assert factors == sorted(factors)


@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -999,
])
def test_factorize_invalid_inputs(invalid_input, factorize):
    with pytest.raises(ValueError):
        factorize(invalid_input)


@pytest.mark.parametrize("invalid_type", [
    "123",
    None,
    [],
    {},
])
def test_factorize_invalid_types(invalid_type, factorize):
    with pytest.raises((TypeError, ValueError)):
        factorize(invalid_type)


@pytest.fixture
def factorize():
    def _factorize(n: int) -> List[int]:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 1:
            raise ValueError("Input must be a positive integer")
            
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
        return fact if fact else []
    
    return _factorize
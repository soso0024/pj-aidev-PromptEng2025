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
from typing import List

def factorize(n: int) -> List[int]:
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

@pytest.mark.parametrize("n,expected", [
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (6, [2, 3]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (10, [2, 5]),
    (12, [2, 2, 3]),
    (15, [3, 5]),
    (16, [2, 2, 2, 2]),
    (17, [17]),
    (18, [2, 3, 3]),
    (20, [2, 2, 5]),
    (25, [5, 5]),
    (30, [2, 3, 5]),
    (36, [2, 2, 3, 3]),
    (49, [7, 7]),
    (50, [2, 5, 5]),
    (60, [2, 2, 3, 5]),
    (100, [2, 2, 5, 5]),
    (121, [11, 11]),
    (144, [2, 2, 2, 2, 3, 3]),
    (169, [13, 13]),
    (200, [2, 2, 2, 5, 5]),
    (225, [3, 3, 5, 5]),
    (256, [2, 2, 2, 2, 2, 2, 2, 2]),
    (289, [17, 17]),
    (300, [2, 2, 3, 5, 5]),
    (361, [19, 19]),
    (400, [2, 2, 2, 2, 5, 5]),
    (500, [2, 2, 5, 5, 5]),
    (1000, [2, 2, 2, 5, 5, 5]),
    (1024, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    (9973, [9973]),
    (9991, [97, 103]),
    (10007, [10007])
])
def test_factorize_valid_numbers(n, expected):
    result = factorize(n)
    assert result == expected
    product = 1
    for factor in result:
        product *= factor
    assert product == n

def test_factorize_edge_case_1():
    result = factorize(1)
    assert result == []

def test_factorize_large_prime():
    result = factorize(97)
    assert result == [97]

def test_factorize_large_composite():
    result = factorize(1001)
    assert result == [7, 11, 13]
    assert 7 * 11 * 13 == 1001

def test_factorize_perfect_squares():
    result = factorize(64)
    assert result == [2, 2, 2, 2, 2, 2]
    assert 2**6 == 64

def test_factorize_product_verification():
    test_cases = [13, 14, 21, 22, 26, 27, 28, 32, 33, 34, 35, 39, 44, 45, 46, 48, 51, 52, 55, 56, 57, 58, 62, 63, 65, 68, 69, 74, 75, 76, 77, 80, 81, 82, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 98, 99]
    for n in test_cases:
        result = factorize(n)
        product = 1
        for factor in result:
            product *= factor
        assert product == n

def test_factorize_all_factors_prime():
    test_cases = [6, 10, 12, 14, 15, 18, 20, 21, 22, 24, 26, 28, 30]
    for n in test_cases:
        result = factorize(n)
        for factor in result:
            assert is_prime(factor)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
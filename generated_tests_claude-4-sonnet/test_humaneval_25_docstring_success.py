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

def factorize(n: int) -> List[int]:
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

def test_factorize_8():
    assert factorize(8) == [2, 2, 2]

def test_factorize_25():
    assert factorize(25) == [5, 5]

def test_factorize_70():
    assert factorize(70) == [2, 5, 7]

def test_factorize_1():
    assert factorize(1) == []

def test_factorize_2():
    assert factorize(2) == [2]

def test_factorize_3():
    assert factorize(3) == [3]

def test_factorize_4():
    assert factorize(4) == [2, 2]

def test_factorize_prime_numbers():
    assert factorize(7) == [7]
    assert factorize(11) == [11]
    assert factorize(13) == [13]
    assert factorize(17) == [17]
    assert factorize(19) == [19]

def test_factorize_large_prime():
    assert factorize(97) == [97]

def test_factorize_composite_numbers():
    assert factorize(12) == [2, 2, 3]
    assert factorize(18) == [2, 3, 3]
    assert factorize(30) == [2, 3, 5]
    assert factorize(60) == [2, 2, 3, 5]

def test_factorize_perfect_squares():
    assert factorize(9) == [3, 3]
    assert factorize(16) == [2, 2, 2, 2]
    assert factorize(36) == [2, 2, 3, 3]
    assert factorize(49) == [7, 7]

def test_factorize_perfect_cubes():
    assert factorize(27) == [3, 3, 3]
    assert factorize(64) == [2, 2, 2, 2, 2, 2]
    assert factorize(125) == [5, 5, 5]

def test_factorize_large_numbers():
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(144) == [2, 2, 2, 2, 3, 3]
    assert factorize(1000) == [2, 2, 2, 5, 5, 5]

def test_factorize_product_equals_original():
    test_cases = [1, 2, 3, 4, 8, 12, 25, 30, 60, 70, 100, 144]
    for n in test_cases:
        factors = factorize(n)
        product = 1
        for factor in factors:
            product *= factor
        assert product == n

@pytest.mark.parametrize("n,expected", [
    (6, [2, 3]),
    (10, [2, 5]),
    (14, [2, 7]),
    (15, [3, 5]),
    (21, [3, 7]),
    (22, [2, 11]),
    (26, [2, 13]),
    (33, [3, 11]),
    (34, [2, 17]),
    (35, [5, 7])
])
def test_factorize_parametrized(n, expected):
    assert factorize(n) == expected

def test_factorize_powers_of_2():
    assert factorize(32) == [2, 2, 2, 2, 2]
    assert factorize(128) == [2, 2, 2, 2, 2, 2, 2]
    assert factorize(256) == [2, 2, 2, 2, 2, 2, 2, 2]

def test_factorize_powers_of_3():
    assert factorize(81) == [3, 3, 3, 3]
    assert factorize(243) == [3, 3, 3, 3, 3]

def test_factorize_mixed_factors():
    assert factorize(72) == [2, 2, 2, 3, 3]
    assert factorize(90) == [2, 3, 3, 5]
    assert factorize(120) == [2, 2, 2, 3, 5]

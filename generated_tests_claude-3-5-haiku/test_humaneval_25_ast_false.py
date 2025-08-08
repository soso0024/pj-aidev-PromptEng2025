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
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return []
    
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
    assert factorize(2) == [2]
    assert factorize(3) == [3]

def test_factorize_composite_number():
    assert factorize(12) == [2, 2, 3]
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(84) == [2, 2, 3, 7]

def test_factorize_large_number():
    assert factorize(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert factorize(123456) == [2, 2, 2, 2, 2, 2, 1929]

def test_factorize_edge_cases():
    assert factorize(1) == []
    assert factorize(0) == []

def test_factorize_negative_number():
    with pytest.raises(ValueError):
        factorize(-10)

@pytest.mark.parametrize("input_num,expected", [
    (12, [2, 2, 3]),
    (100, [2, 2, 5, 5]),
    (17, [17]),
    (1, []),
    (2, [2]),
    (84, [2, 2, 3, 7])
])
def test_factorize_parametrized(input_num, expected):
    assert factorize(input_num) == expected
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

def test_factorize_positive_integers():
    assert factorize(1) == [1]
    assert factorize(2) == [2]
    assert factorize(12) == [2, 2, 3]
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(999) == [3, 3, 37]

def test_factorize_negative_integers():
    with pytest.raises(ValueError):
        factorize(-1)

def test_factorize_zero():
    with pytest.raises(ValueError):
        factorize(0)

def test_factorize_float():
    with pytest.raises(TypeError):
        factorize(3.14)

def test_factorize_string():
    with pytest.raises(TypeError):
        factorize("42")

@pytest.mark.parametrize("input,expected", [
    (1, [1]),
    (2, [2]),
    (12, [2, 2, 3]),
    (100, [2, 2, 5, 5]),
    (999, [3, 3, 37]),
    (-1, pytest.raises(ValueError)),
    (0, pytest.raises(ValueError)),
    (3.14, pytest.raises(TypeError)),
    ("42", pytest.raises(TypeError))
])
def test_factorize_all_cases(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            factorize(input)
    else:
        assert factorize(input) == expected
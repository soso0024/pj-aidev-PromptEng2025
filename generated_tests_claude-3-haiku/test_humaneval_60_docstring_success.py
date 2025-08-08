# Test cases for HumanEval/60
# Generated using Claude API



def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    return sum(range(n + 1))


# Generated test cases:
import pytest
from math import isclose

@pytest.mark.parametrize("n,expected", [
    (30, 465),
    (100, 5050),
    (5, 15),
    (10, 55),
    (1, 1),
    (0, 0),
    (-1, 0),
    (3, 6),
    (10, 55)
])
def test_sum_to_n(n, expected):
    try:
        result = sum_to_n(n)
        if isinstance(expected, float):
            assert isclose(result, expected)
        else:
            assert result == expected
    except TypeError:
        assert isinstance(n, int)

def sum_to_n(n: int):
    if not isinstance(n, int):
        raise TypeError
    return sum(range(n + 1))
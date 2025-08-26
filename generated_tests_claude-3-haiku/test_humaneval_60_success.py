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

def test_sum_to_n_positive():
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(100) == 5050

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_negative():
    with pytest.raises(ValueError):
        sum_to_n(-1)

@pytest.mark.parametrize("n,expected", [
    (5, 15),
    (10, 55),
    (100, 5050),
    (0, 0),
    (-1, ValueError)
])
def test_sum_to_n_parametrized(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            sum_to_n(n)
    else:
        assert sum_to_n(n) == expected

def sum_to_n(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return sum(range(n + 1))
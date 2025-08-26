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

def sum_to_n(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return sum(range(n + 1))

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_positive():
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55

def test_sum_to_n_large_number():
    assert sum_to_n(100) == 5050

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (5, 15),
    (10, 55),
    (100, 5050)
])
def test_sum_to_n_parametrized(n, expected):
    assert sum_to_n(n) == expected

def test_sum_to_n_negative():
    with pytest.raises(ValueError):
        sum_to_n(-1)

def test_sum_to_n_type_error():
    with pytest.raises(TypeError):
        sum_to_n("not a number")
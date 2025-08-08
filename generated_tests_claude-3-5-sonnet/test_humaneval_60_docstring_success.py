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

def test_sum_to_n_basic():
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1

@pytest.mark.parametrize("n,expected", [
    (30, 465),
    (100, 5050),
    (0, 0),
    (2, 3),
    (3, 6),
])
def test_sum_to_n_parametrized(n, expected):
    assert sum_to_n(n) == expected

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_single():
    assert sum_to_n(1) == 1

def test_sum_to_n_negative():
    result = sum_to_n(-1)
    assert result == 0

def test_sum_to_n_type_error():
    with pytest.raises(TypeError):
        sum_to_n("not a number")
    with pytest.raises(TypeError):
        sum_to_n(3.14)
    with pytest.raises(TypeError):
        sum_to_n(None)

def test_sum_to_n_large_number():
    assert sum_to_n(1000) == 500500

def test_sum_to_n_boundary():
    assert sum_to_n(999999) == 499999500000
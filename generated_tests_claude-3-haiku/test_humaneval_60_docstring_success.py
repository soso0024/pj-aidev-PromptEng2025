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

def test_sum_to_n_positive_integers():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (-5, 0),
    (3, 6),
    ('string', TypeError),
    (None, TypeError)
])
def test_sum_to_n_edge_cases(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            sum_to_n(n)
    else:
        assert sum_to_n(n) == expected
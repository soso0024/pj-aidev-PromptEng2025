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
    (-1, ValueError),
    (0, 0),
    (3.14, TypeError),
    ('10', TypeError)
])
def test_sum_to_n_edge_cases(n, expected):
    if expected == ValueError:
        with pytest.raises(expected):
            sum_to_n(n)
    elif expected == TypeError:
        with pytest.raises(expected):
            sum_to_n(n)
    else:
        assert sum_to_n(n) == expected
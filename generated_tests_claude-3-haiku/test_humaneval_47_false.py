# Test cases for HumanEval/47
# Generated using Claude API



def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


# Generated test cases:
import pytest

def test_median_empty_list():
    with pytest.raises(ValueError):
        median([])

def test_median_single_element():
    assert median([5]) == 5

def test_median_even_length():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 3, 4, 5, 6]) == 3.5

def test_median_odd_length():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4, 5]) == 3

def test_median_sorted_list():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6, 7]) == 4

def test_median_unsorted_list():
    assert median([5, 2, 1, 4, 3]) == 3
    assert median([6, 2, 1, 4, 3, 5]) == 3.5

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([5, 2, 1, 4, 3], 3),
    ([6, 2, 1, 4, 3, 5], 3.5),
    ([], ValueError)
])
def test_median_parametrized(input_list, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            median(input_list)
    else:
        assert median(input_list) == expected
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

def test_median_odd_length_list():
    assert median([1, 3, 5]) == 3
    assert median([7, 3, 1, 4, 2]) == 3
    assert median([-1, 0, 1]) == 0

def test_median_even_length_list():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([2, 4, 6, 8]) == 5.0
    assert median([-2, -1, 1, 2]) == 0.5

def test_median_single_element():
    assert median([42]) == 42

def test_median_floating_point():
    assert median([1.5, 2.5, 3.5]) == 2.5

def test_median_negative_numbers():
    assert median([-5, -3, -1, 0, 2]) == -1

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40], 25.0),
    ([-1, 0, 1], 0),
    ([100], 100)
])
def test_median_parametrized(input_list, expected):
    assert median(input_list) == expected

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])
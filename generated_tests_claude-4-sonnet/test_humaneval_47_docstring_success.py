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

def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

def test_median_odd_length():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([1]) == 1
    assert median([5, 2, 8]) == 5

def test_median_even_length():
    assert median([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert median([1, 2]) == 1.5
    assert median([1, 2, 3, 4]) == 2.5

def test_median_negative_numbers():
    assert median([-5, -3, -1]) == -3
    assert median([-10, -5, -2, -1]) == -3.5
    assert median([-1, -2, -3, -4, -5]) == -3

def test_median_mixed_positive_negative():
    assert median([-2, -1, 0, 1, 2]) == 0
    assert median([-5, 0, 5, 10]) == 2.5

def test_median_duplicates():
    assert median([1, 1, 1]) == 1
    assert median([2, 2, 2, 2]) == 2.0
    assert median([1, 2, 2, 3]) == 2.0

def test_median_floats():
    assert median([1.5, 2.5, 3.5]) == 2.5
    assert median([1.1, 2.2, 3.3, 4.4]) == 2.75

def test_median_large_numbers():
    assert median([1000000, 2000000, 3000000]) == 2000000
    assert median([999999, 1000000]) == 999999.5

def test_median_zero():
    assert median([0]) == 0
    assert median([0, 0]) == 0.0
    assert median([-1, 0, 1]) == 0

def test_median_unsorted_input():
    assert median([5, 1, 9, 3, 7]) == 5
    assert median([10, 2, 8, 4, 6]) == 6

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([5], 5),
    ([0, 0, 0], 0),
    ([-1, -2, -3], -2),
    ([100, 200], 150.0)
])
def test_median_parametrized(input_list, expected):
    assert median(input_list) == expected
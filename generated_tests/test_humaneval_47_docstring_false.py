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
from typing import List

@pytest.mark.parametrize("input_list,expected", [
    ([3, 1, 2, 4, 5], 3),
    ([-10, 4, 6, 1000, 10, 20], 15.0),
    ([1], 1),
    ([1, 2], 1.5),
    ([1, 2, 3, 4], 2.5),
    ([-5, -3, -1, -2, -4], -3),
    ([100, 100, 100, 100, 100], 100),
    ([0.5, 1.5, 2.5, 3.5], 2.0),
    ([float("inf"), 1, 2, 3], 2.5),
    ([-float("inf"), 1, 2, 3], 1.5),
])
def test_median_valid_inputs(input_list, expected):
    assert median(input_list) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3],
    [[], 2, 3],
    [{1: 1}, 2, 3],
])
def test_median_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        median(invalid_input)

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])

def test_median_large_list():
    large_list = list(range(1000))
    assert median(large_list) == 499.5

def test_median_duplicate_values():
    assert median([1, 1, 1, 2, 2, 2]) == 1.5

def test_median_negative_and_positive():
    assert median([-5, -2, 0, 3, 7]) == 0

def test_median_floating_point():
    assert abs(median([1.1, 2.2, 3.3, 4.4]) - 2.75) < 1e-10

def test_median_single_element():
    assert median([42]) == 42

def test_median_two_elements():
    assert median([1, 2]) == 1.5

def test_median_unsorted_input():
    assert median([5, 2, 1, 4, 3]) == 3
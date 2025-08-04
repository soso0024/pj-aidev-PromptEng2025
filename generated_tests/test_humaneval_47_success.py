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
import math

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([3, 1, 2], 2),
    ([4, 2, 1, 3], 2.5),
    ([1], 1),
    ([1.5, 2.5], 2.0),
    ([-1, -2, -3], -2),
    ([0, 0, 0], 0),
    ([1, 1, 1, 1], 1),
    ([float('inf'), 1, 2], 2),
    ([-float('inf'), 1, 2], 1),
    ([2.5, 1.5, 3.5, 4.5], 3.0)
])
def test_median_valid_inputs(input_list, expected):
    assert median(input_list) == expected

def test_median_empty_list():
    with pytest.raises(IndexError):
        median([])

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    {"a": 1, "b": 2}
])
def test_median_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        median(invalid_input)

def test_median_large_numbers():
    assert median([10**10, 10**11, 10**12]) == 10**11

def test_median_mixed_numbers():
    assert median([1, -1, 0.5, -0.5]) == 0.0

def test_median_single_element():
    assert median([42]) == 42

def test_median_duplicate_values():
    assert median([1, 1, 2, 2]) == 1.5

def test_median_float_precision():
    assert abs(median([1.1, 2.2, 3.3]) - 2.2) < 1e-10

def test_median_set_input():
    test_set = {1, 2, 3}
    assert median(list(test_set)) == 2
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
    ([3, 1, 2, 4, 5], 3),
    ([-10, 4, 6, 1000, 10, 20], 8.0),
    ([1], 1),
    ([1, 2], 1.5),
    ([1, 2, 3, 4], 2.5),
    ([-5, -3, -1, -2, -4], -3),
    ([0, 0, 0, 0, 0], 0),
    ([1.5, 2.5, 3.5], 2.5),
    ([float('inf'), 1, 2], 2),
    ([-float('inf'), 1, 2], 1),
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

@pytest.mark.parametrize("input_list", [
    [None, 1, 2],
    [1, "string", 3],
    [1, [], 3],
    [1, {}, 3]
])
def test_median_mixed_types(input_list):
    with pytest.raises(TypeError):
        median(input_list)

def test_median_large_list():
    large_list = list(range(1000000))
    assert median(large_list) == 499999.5

def test_median_duplicate_values():
    assert median([1, 1, 1, 1, 2]) == 1
    assert median([1, 2, 2, 2, 2]) == 2
    assert median([1, 1, 2, 2]) == 1.5

def test_median_floating_point():
    assert math.isclose(median([1.1, 2.2, 3.3]), 2.2, rel_tol=1e-9)
    assert math.isclose(median([1.1, 2.2, 3.3, 4.4]), 2.75, rel_tol=1e-9)
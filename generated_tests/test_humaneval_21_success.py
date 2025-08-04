# Test cases for HumanEval/21
# Generated using Claude API

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


# Generated test cases:
import pytest
from typing import List
import math

def test_rescale_basic():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

def test_rescale_single_value():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([2.0])

def test_rescale_negative_numbers():
    assert rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]

def test_rescale_same_numbers():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([1.0, 1.0, 1.0])

def test_rescale_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

@pytest.mark.parametrize("input_list,expected", [
    ([0.0, 5.0, 10.0], [0.0, 0.5, 1.0]),
    ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0]),
    ([1.5, 2.5, 3.5, 4.5], [0.0, 1/3, 2/3, 1.0]),
    ([100.0, 200.0, 300.0, 400.0], [0.0, 1/3, 2/3, 1.0])
])
def test_rescale_parametrized(input_list, expected):
    result = rescale_to_unit(input_list)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)

def test_rescale_floating_point_precision():
    result = rescale_to_unit([0.1, 0.2, 0.3])
    expected = [0.0, 0.5, 1.0]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)

def test_rescale_large_numbers():
    result = rescale_to_unit([1e6, 2e6, 3e6])
    expected = [0.0, 0.5, 1.0]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)

def test_rescale_small_numbers():
    result = rescale_to_unit([1e-6, 2e-6, 3e-6])
    expected = [0.0, 0.5, 1.0]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)

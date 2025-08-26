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
import math
from typing import List

def test_rescale_to_unit_basic():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_single_value():
    assert rescale_to_unit([5.0, 5.0]) == [0.5, 0.5]

def test_rescale_to_unit_negative_numbers():
    assert rescale_to_unit([-10.0, -5.0, 0.0, 5.0, 10.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_too_few_elements():
    with pytest.raises(ValueError):
        rescale_to_unit([1.0])

def test_rescale_to_unit_infinity():
    with pytest.raises(ValueError):
        rescale_to_unit([1.0, float('inf')])

def test_rescale_to_unit_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])
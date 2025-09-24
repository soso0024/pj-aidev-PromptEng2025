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
from typing import List
import pytest

def test_rescale_to_unit_empty_list():
    assert rescale_to_unit([]) == []

def test_rescale_to_unit_single_element():
    assert rescale_to_unit([5.0]) == [0.0]

def test_rescale_to_unit_all_equal():
    assert rescale_to_unit([10.0, 10.0, 10.0]) == [0.0, 0.0, 0.0]

def test_rescale_to_unit_positive_numbers():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]

def test_rescale_to_unit_negative_numbers():
    assert rescale_to_unit([-5.0, -3.0, -1.0]) == [0.0, 0.5, 1.0]

def test_rescale_to_unit_mixed_numbers():
    assert rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]

def test_rescale_to_unit_float_precision():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == pytest.approx([0.0, 0.5, 1.0])

def test_rescale_to_unit_type_error():
    with pytest.raises(TypeError):
        rescale_to_unit([1, 2, 3])

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0] * len(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]
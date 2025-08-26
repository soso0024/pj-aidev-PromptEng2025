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

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    min_number = min(numbers)
    max_number = max(numbers)
    
    if min_number == max_number:
        return [0.5] * len(numbers)
    
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_to_unit_normal_case():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_single_repeated_value():
    assert rescale_to_unit([5.0, 5.0, 5.0]) == [0.5, 0.5, 0.5]

def test_rescale_to_unit_negative_numbers():
    assert rescale_to_unit([-10.0, -5.0, 0.0, 5.0, 10.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_floating_point():
    result = rescale_to_unit([1.5, 2.7, 3.2, 4.1, 5.0])
    assert all(0.0 <= x <= 1.0 for x in result)
    assert result[0] == 0.0
    assert result[-1] == 1.0

@pytest.mark.parametrize("input_list,expected", [
    ([1.0, 2.0], [0.0, 1.0]),
    ([0.0, 10.0], [0.0, 1.0]),
    ([-5.0, 5.0], [0.0, 1.0])
])
def test_rescale_to_unit_parametrized(input_list, expected):
    assert rescale_to_unit(input_list) == expected

def test_rescale_to_unit_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

def test_rescale_to_unit_single_element():
    with pytest.raises(ValueError):
        rescale_to_unit([42.0])
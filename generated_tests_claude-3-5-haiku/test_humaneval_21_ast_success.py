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

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    min_number = min(numbers)
    max_number = max(numbers)
    
    if min_number == max_number:
        return [0.5] * len(numbers)
    
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_to_unit_normal_case():
    input_list = [1, 2, 3, 4, 5]
    result = rescale_to_unit(input_list)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_single_element():
    input_list = [42]
    result = rescale_to_unit(input_list)
    assert result == [0.5]

def test_rescale_to_unit_negative_numbers():
    input_list = [-10, -5, 0, 5, 10]
    result = rescale_to_unit(input_list)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_float_numbers():
    input_list = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = rescale_to_unit(input_list)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_rescale_to_unit_all_same_value():
    input_list = [7, 7, 7, 7]
    result = rescale_to_unit(input_list)
    assert result == [0.5, 0.5, 0.5, 0.5]

def test_rescale_to_unit_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

@pytest.mark.parametrize("input_list", [
    [0, 0, 0],
    [-1, -1, -1],
    [100, 100, 100]
])
def test_rescale_to_unit_constant_list(input_list):
    result = rescale_to_unit(input_list)
    assert result == [0.5, 0.5, 0.5]
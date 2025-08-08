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

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) == 0:
        raise ValueError("Cannot rescale an empty list")
    
    if len(set(numbers)) == 1:
        return [0.5] * len(numbers)
    
    if any(math.isinf(x) or math.isnan(x) for x in numbers):
        raise ValueError("Cannot rescale list with infinite or NaN values")
    
    min_number = min(numbers)
    max_number = max(numbers)
    
    if len(numbers) == 1:
        return [1.0]
    
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_to_unit_normal_case():
    input_list = [1, 2, 3, 4, 5]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == pytest.approx(expected)

def test_rescale_to_unit_single_element():
    input_list = [42]
    expected = [1.0]
    assert rescale_to_unit(input_list) == pytest.approx(expected)

def test_rescale_to_unit_negative_numbers():
    input_list = [-10, -5, 0, 5, 10]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == pytest.approx(expected)

def test_rescale_to_unit_floating_point():
    input_list = [1.5, 2.7, 3.2, 4.1, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == pytest.approx(expected)

def test_rescale_to_unit_all_same_value():
    input_list = [7, 7, 7, 7]
    expected = [0.5, 0.5, 0.5, 0.5]
    assert rescale_to_unit(input_list) == pytest.approx(expected)

def test_rescale_to_unit_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

@pytest.mark.parametrize("input_list", [
    [float('inf'), float('inf')],
    [float('-inf'), float('-inf')],
    [float('nan'), float('nan')]
])
def test_rescale_to_unit_special_float_values(input_list):
    with pytest.raises(ValueError):
        rescale_to_unit(input_list)
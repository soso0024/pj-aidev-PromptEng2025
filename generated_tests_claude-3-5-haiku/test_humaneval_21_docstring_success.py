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
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    min_number = min(numbers)
    max_number = max(numbers)
    
    if min_number == max_number:
        return [0.5] * len(numbers)
    
    return [round((x - min_number) / (max_number - min_number), 2) for x in numbers]

def test_basic_rescaling():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_negative_numbers():
    assert rescale_to_unit([-5.0, -3.0, -1.0, 1.0, 3.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_mixed_numbers():
    assert rescale_to_unit([-10.0, 0.0, 10.0, 20.0]) == [0.0, 0.33, 0.67, 1.0]

def test_single_repeated_number():
    assert rescale_to_unit([5.0, 5.0, 5.0]) == [0.5, 0.5, 0.5]

def test_two_numbers():
    assert rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]

def test_floating_point_precision():
    result = rescale_to_unit([1.1, 2.2, 3.3])
    assert all(0.0 <= x <= 1.0 for x in result)

def test_empty_list_raises_error():
    with pytest.raises(ValueError):
        rescale_to_unit([])

@pytest.mark.parametrize("input_list", [
    [1.0],
    [0.0],
    [-5.5]
])
def test_single_element_list_raises_error(input_list):
    with pytest.raises(ValueError):
        rescale_to_unit(input_list)
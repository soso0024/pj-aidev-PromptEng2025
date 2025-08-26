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

def test_rescale_to_unit_normal_case():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected

def test_rescale_to_unit_empty_list():
    numbers = []
    expected = []
    assert rescale_to_unit(numbers) == expected

def test_rescale_to_unit_single_element():
    numbers = [10.0]
    expected = [0.0]
    assert rescale_to_unit(numbers) == expected

@pytest.mark.parametrize("numbers,expected", [
    ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0]),
    ([-1.0, 0.0, 1.0], [0.0, 0.5, 1.0]),
    ([1.0, 2.0, 3.0, 4.0, 5.0], [0.0, 0.25, 0.5, 0.75, 1.0]),
    ([-5.0, -4.0, -3.0, -2.0, -1.0], [0.0, 0.25, 0.5, 0.75, 1.0]),
])
def test_rescale_to_unit_parametrized(numbers, expected):
    assert rescale_to_unit(numbers) == expected

def test_rescale_to_unit_with_non_numeric_input():
    with pytest.raises(TypeError):
        rescale_to_unit([1.0, 2.0, 'a', 4.0])
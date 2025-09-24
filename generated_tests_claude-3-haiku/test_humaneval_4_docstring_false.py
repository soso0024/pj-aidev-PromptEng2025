# Test cases for HumanEval/4
# Generated using Claude API

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


# Generated test cases:
import pytest
from typing import List

def test_mean_absolute_deviation_empty_list():
    assert mean_absolute_deviation([]) == 0.0

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

@pytest.mark.parametrize("input,expected", [
    ([1.0, 2.0, 3.0, 4.0], 1.0),
    ([0.0, 2.0, 4.0, 6.0], 2.0),
    ([-1.0, 1.0, 3.0, 5.0], 2.0),
    ([2.5, 2.5, 2.5, 2.5], 0.0)
])
def test_mean_absolute_deviation_various_inputs(input, expected):
    assert mean_absolute_deviation(input) == expected

def test_mean_absolute_deviation_with_negative_numbers():
    assert abs(mean_absolute_deviation([-2.0, -1.0, 0.0, 1.0, 2.0]) - 1.0) < 1e-6

def test_mean_absolute_deviation_with_zero():
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0
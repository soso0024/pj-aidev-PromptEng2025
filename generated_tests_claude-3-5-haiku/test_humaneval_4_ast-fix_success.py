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

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ZeroDivisionError("Cannot calculate mean absolute deviation of an empty list")
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def test_mean_absolute_deviation_normal_case():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([42]) == 0.0

def test_mean_absolute_deviation_negative_numbers():
    assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2

def test_mean_absolute_deviation_mixed_numbers():
    assert round(mean_absolute_deviation([-10, 0, 10]), 2) == 6.67

def test_mean_absolute_deviation_floating_point():
    assert round(mean_absolute_deviation([1.5, 2.5, 3.5]), 2) == 0.67

def test_mean_absolute_deviation_zero_values():
    assert mean_absolute_deviation([0, 0, 0, 0]) == 0.0

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 1.2),
    ([-1, -2, -3, -4, -5], 1.2),
    ([0, 0, 0, 0], 0.0),
    ([1.5, 2.5, 3.5], 0.67)
])
def test_mean_absolute_deviation_parametrized(input_list, expected):
    assert round(mean_absolute_deviation(input_list), 2) == expected
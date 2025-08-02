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
import math
from typing import List

@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4, 5], 1.2),
    ([2, 2, 2, 2], 0.0),
    ([1, 1, 1, 2], 0.375),
    ([0, 10], 5.0),
    ([-1, 1], 1.0),
    ([1.5, 2.5, 3.5], 0.6666666666666666),
])
def test_mean_absolute_deviation_normal_cases(numbers, expected):
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

@pytest.mark.parametrize("numbers,expected", [
    ([0], 0.0),
    ([42], 0.0),
    ([-99], 0.0),
])
def test_mean_absolute_deviation_single_number(numbers, expected):
    assert mean_absolute_deviation(numbers) == expected

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

@pytest.mark.parametrize("numbers", [
    [float('inf'), 1, 2],
    [float('-inf'), 1, 2],
    [float('nan'), 1, 2],
])
def test_mean_absolute_deviation_special_floats(numbers):
    result = mean_absolute_deviation(numbers)
    assert math.isnan(result)

def test_mean_absolute_deviation_large_numbers():
    numbers = [1e15, 1e15 + 1, 1e15 + 2]
    expected = 0.6666666666666666
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

def test_mean_absolute_deviation_small_numbers():
    numbers = [1e-15, 1e-15 + 1e-15, 1e-15 + 2e-15]
    expected = 6.666666666666667e-16
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

def test_mean_absolute_deviation_type_error():
    with pytest.raises(TypeError):
        mean_absolute_deviation(['1', '2', '3'])

def test_mean_absolute_deviation_none_input():
    with pytest.raises(TypeError):
        mean_absolute_deviation(None)

def mean_absolute_deviation(numbers: List[float]) -> float:
    if numbers is None:
        raise TypeError("Input cannot be None")
    if not numbers:
        raise ZeroDivisionError("Cannot calculate MAD of empty list")
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
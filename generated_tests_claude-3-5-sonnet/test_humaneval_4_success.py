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
import math

@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4, 5], 1.2),
    ([2, 2, 2, 2], 0.0),
    ([1.5, 2.5, 3.5], 0.6666666666666666),
    ([0, 0, 0], 0.0),
    ([-1, 0, 1], 0.6666666666666666),
    ([-2, -1, 0, 1, 2], 1.2),
    ([10.5, -10.5], 10.5),
])
def test_mean_absolute_deviation_normal_cases(numbers, expected):
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

@pytest.mark.parametrize("numbers", [
    [1.0],
    [42.0],
    [-3.14],
])
def test_mean_absolute_deviation_single_number(numbers):
    assert mean_absolute_deviation(numbers) == 0.0

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    42,
    3.14,
    [1, "2", 3],
    [[], [], []],
    [[1, 2], [3, 4]],
])
def test_mean_absolute_deviation_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        mean_absolute_deviation(invalid_input)

def test_mean_absolute_deviation_large_numbers():
    numbers = [1e6, 2e6, 3e6, 4e6]
    expected = 1e6
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

def test_mean_absolute_deviation_small_numbers():
    numbers = [1e-6, 2e-6, 3e-6, 4e-6]
    expected = 1e-6
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

def test_mean_absolute_deviation_mixed_signs():
    numbers = [-1e3, 1e3, -1e3, 1e3]
    expected = 1e3
    assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)

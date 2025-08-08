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

def test_basic_list():
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == pytest.approx(0.6666666666666666)

def test_single_number():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_negative_numbers():
    assert mean_absolute_deviation([-2.0, -1.0, 0.0, 1.0, 2.0]) == pytest.approx(1.2)

def test_identical_numbers():
    assert mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]) == 0.0

def test_decimal_numbers():
    assert mean_absolute_deviation([1.5, 2.5, 3.5]) == pytest.approx(0.6666666666666666)

@pytest.mark.parametrize("numbers, expected", [
    ([0.0, 0.0, 0.0], 0.0),
    ([1.0, -1.0], 1.0),
    ([10.0, 20.0, 30.0, 40.0], 10.0),
    ([0.1, 0.2, 0.3], pytest.approx(0.0666666666666667))
])
def test_various_cases(numbers, expected):
    assert mean_absolute_deviation(numbers) == expected

def test_large_numbers():
    assert mean_absolute_deviation([1000.0, 2000.0, 3000.0]) == pytest.approx(666.6666666666666)

@pytest.mark.parametrize("invalid_input", [
    [],
    None,
    ["1", "2", "3"],
    [1, 2, "3"]
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((ValueError, TypeError, ZeroDivisionError)):
        mean_absolute_deviation(invalid_input)

def test_floating_point_precision():
    result = mean_absolute_deviation([0.1, 0.2, 0.3, 0.4, 0.5])
    assert math.isclose(result, 0.12, rel_tol=1e-9)

def test_very_small_numbers():
    assert mean_absolute_deviation([0.0001, 0.0002, 0.0003]) == pytest.approx(0.00006666666666666667)

def test_mixed_positive_negative():
    assert mean_absolute_deviation([-10.5, 15.5, -20.5, 25.5]) == pytest.approx(18.0)

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers or not isinstance(numbers, list):
        raise ValueError("Input must be a non-empty list")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
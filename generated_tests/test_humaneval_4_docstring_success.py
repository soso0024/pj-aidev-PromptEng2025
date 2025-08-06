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


def test_basic_list():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0


def test_single_number():
    assert mean_absolute_deviation([5.0]) == 0.0


def test_negative_numbers():
    assert abs(mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]) - 1.5) < 1e-10


def test_identical_numbers():
    assert mean_absolute_deviation([3.0, 3.0, 3.0]) == 0.0


@pytest.mark.parametrize("numbers, expected", [
    ([1.0, 1.0, 1.0, 1.0], 0.0),
    ([0.0, 10.0], 5.0),
    ([1.5, 2.5, 3.5], 0.6666666666666666),
    ([-5.0, 5.0], 5.0),
])
def test_various_inputs(numbers, expected):
    assert abs(mean_absolute_deviation(numbers) - expected) < 1e-10


def test_decimal_numbers():
    assert abs(mean_absolute_deviation([0.1, 0.2, 0.3, 0.4]) - 0.1) < 1e-10


@pytest.mark.parametrize("invalid_input", [
    [],
    None,
    ["1.0", "2.0"],
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((ZeroDivisionError, TypeError, AttributeError)):
        mean_absolute_deviation(invalid_input)


def test_integer_inputs():
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    assert abs(result - 0.6666666666666666) < 1e-10


def test_large_numbers():
    assert abs(mean_absolute_deviation([1e6, 2e6, 3e6]) - 666666.6666666666) < 1e-6


def test_small_numbers():
    assert abs(mean_absolute_deviation([1e-6, 2e-6, 3e-6]) - 6.666666666666667e-7) < 1e-10


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
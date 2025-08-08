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


def test_repeated_numbers():
    assert mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0


@pytest.mark.parametrize("numbers, expected", [
    ([1.0, 1.0, 1.0], 0.0),
    ([0.0, 10.0], 5.0),
    ([1.5, 2.5, 3.5], 0.6666666666666666),
    ([-1.0, 0.0, 1.0], 0.6666666666666666)
])
def test_various_inputs(numbers, expected):
    assert abs(mean_absolute_deviation(numbers) - expected) < 1e-10


def test_decimal_numbers():
    assert abs(mean_absolute_deviation([0.1, 0.2, 0.3, 0.4]) - 0.1) < 1e-10


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_empty_list():
    mean_absolute_deviation([])


@pytest.mark.xfail(raises=TypeError)
def test_invalid_input_types():
    mean_absolute_deviation(['a', 'b', 'c'])


@pytest.mark.xfail(raises=TypeError)
def test_none_input():
    mean_absolute_deviation(None)


def test_large_numbers():
    assert abs(mean_absolute_deviation([1000000.0, 2000000.0, 3000000.0]) - 666666.6666666666) < 1e-10


def test_small_numbers():
    assert abs(mean_absolute_deviation([0.0001, 0.0002, 0.0003]) - 0.00006666666666666667) < 1e-10

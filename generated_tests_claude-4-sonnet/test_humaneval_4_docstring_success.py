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
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def test_mean_absolute_deviation_basic():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_mean_absolute_deviation_two_elements():
    assert mean_absolute_deviation([1.0, 3.0]) == 1.0

def test_mean_absolute_deviation_identical_elements():
    assert mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0

def test_mean_absolute_deviation_negative_numbers():
    result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
    assert abs(result - 1.0) < 1e-10

def test_mean_absolute_deviation_mixed_positive_negative():
    result = mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0])
    assert abs(result - 1.5) < 1e-10

def test_mean_absolute_deviation_zeros():
    assert mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0

def test_mean_absolute_deviation_with_zero():
    result = mean_absolute_deviation([0.0, 1.0, 2.0])
    expected = 2.0/3.0
    assert abs(result - expected) < 1e-10

def test_mean_absolute_deviation_large_numbers():
    result = mean_absolute_deviation([100.0, 200.0, 300.0])
    assert abs(result - 66.66666666666667) < 1e-10

def test_mean_absolute_deviation_decimal_numbers():
    result = mean_absolute_deviation([1.5, 2.5, 3.5])
    assert abs(result - 0.6666666666666666) < 1e-10

def test_mean_absolute_deviation_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

@pytest.mark.parametrize("numbers,expected", [
    ([1.0], 0.0),
    ([5.0, 5.0], 0.0),
    ([0.0, 2.0], 1.0),
    ([1.0, 2.0, 3.0], 0.6666666666666666),
    ([-1.0, 0.0, 1.0], 0.6666666666666666),
])
def test_mean_absolute_deviation_parametrized(numbers, expected):
    result = mean_absolute_deviation(numbers)
    assert abs(result - expected) < 1e-10

def test_mean_absolute_deviation_very_small_numbers():
    result = mean_absolute_deviation([0.001, 0.002, 0.003])
    expected = 0.0006666666666666666
    assert abs(result - expected) < 1e-15

def test_mean_absolute_deviation_large_dataset():
    numbers = list(range(1, 101))
    numbers = [float(x) for x in numbers]
    result = mean_absolute_deviation(numbers)
    assert abs(result - 25.0) < 1e-10

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

def mean_absolute_deviation(numbers: List[float]):
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

def test_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_two_identical_elements():
    assert mean_absolute_deviation([3.0, 3.0]) == 0.0

def test_two_different_elements():
    result = mean_absolute_deviation([1.0, 3.0])
    assert abs(result - 1.0) < 1e-10

def test_three_elements():
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    expected = 2.0 / 3.0
    assert abs(result - expected) < 1e-10

def test_negative_numbers():
    result = mean_absolute_deviation([-1.0, -2.0, -3.0])
    expected = 2.0 / 3.0
    assert abs(result - expected) < 1e-10

def test_mixed_positive_negative():
    result = mean_absolute_deviation([-2.0, 0.0, 2.0])
    expected = 4.0 / 3.0
    assert abs(result - expected) < 1e-10

def test_zeros():
    assert mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0

def test_large_numbers():
    result = mean_absolute_deviation([1000.0, 2000.0, 3000.0])
    expected = 2000.0 / 3.0
    assert abs(result - expected) < 1e-6

def test_small_decimal_numbers():
    result = mean_absolute_deviation([0.1, 0.2, 0.3])
    expected = 2.0 / 30.0
    assert abs(result - expected) < 1e-10

def test_integers_as_floats():
    result = mean_absolute_deviation([1.0, 4.0, 7.0])
    expected = 2.0
    assert abs(result - expected) < 1e-10

@pytest.mark.parametrize("numbers,expected", [
    ([5.0], 0.0),
    ([1.0, 1.0], 0.0),
    ([0.0, 0.0, 0.0, 0.0], 0.0),
    ([2.0, 4.0], 1.0),
    ([-1.0, 1.0], 1.0)
])
def test_parametrized_cases(numbers, expected):
    result = mean_absolute_deviation(numbers)
    assert abs(result - expected) < 1e-10

def test_empty_list_raises_error():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_very_large_list():
    numbers = [float(i) for i in range(1000)]
    result = mean_absolute_deviation(numbers)
    assert result > 0
    assert isinstance(result, float)

def test_all_same_values():
    numbers = [42.0] * 100
    assert mean_absolute_deviation(numbers) == 0.0

def test_extreme_values():
    result = mean_absolute_deviation([1e-10, 1e10])
    assert result > 0
    assert isinstance(result, float)

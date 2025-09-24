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
import pytest
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_basic_case():
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert result == expected

def test_rescale_two_elements():
    result = rescale_to_unit([10.0, 20.0])
    expected = [0.0, 1.0]
    assert result == expected

def test_rescale_negative_numbers():
    result = rescale_to_unit([-5.0, -2.0, 0.0, 3.0])
    expected = [0.0, 0.375, 0.625, 1.0]
    assert result == expected

def test_rescale_all_negative():
    result = rescale_to_unit([-10.0, -5.0, -1.0])
    expected = [0.0, 5.0/9.0, 1.0]
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

def test_rescale_decimal_values():
    result = rescale_to_unit([0.1, 0.3, 0.7, 0.9])
    expected = [0.0, 0.25, 0.75, 1.0]
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

def test_rescale_large_numbers():
    result = rescale_to_unit([1000.0, 2000.0, 3000.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_unsorted_list():
    result = rescale_to_unit([3.0, 1.0, 4.0, 2.0])
    expected = [2.0/3.0, 0.0, 1.0, 1.0/3.0]
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

def test_rescale_with_zero():
    result = rescale_to_unit([0.0, 5.0, 10.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_fractional_range():
    result = rescale_to_unit([0.1, 0.2, 0.3])
    expected = [0.0, 0.5, 1.0]
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

@pytest.mark.parametrize("numbers,expected", [
    ([1.0, 3.0], [0.0, 1.0]),
    ([10.0, 5.0, 15.0], [0.5, 0.0, 1.0]),
    ([-1.0, 1.0], [0.0, 1.0]),
    ([100.0, 200.0, 300.0, 400.0], [0.0, 1.0/3.0, 2.0/3.0, 1.0])
])
def test_rescale_parametrized(numbers, expected):
    result = rescale_to_unit(numbers)
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10
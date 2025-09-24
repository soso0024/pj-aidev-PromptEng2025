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

def rescale_to_unit(numbers: List[float]):
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

def test_rescale_basic_positive_numbers():
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert result == expected

def test_rescale_negative_numbers():
    result = rescale_to_unit([-5.0, -3.0, -1.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_mixed_positive_negative():
    result = rescale_to_unit([-2.0, 0.0, 2.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_single_element():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0])

def test_rescale_all_same_values():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([3.0, 3.0, 3.0])

def test_rescale_two_elements():
    result = rescale_to_unit([1.0, 5.0])
    expected = [0.0, 1.0]
    assert result == expected

def test_rescale_decimal_numbers():
    result = rescale_to_unit([0.1, 0.5, 0.9])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_large_numbers():
    result = rescale_to_unit([1000.0, 2000.0, 3000.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_very_small_numbers():
    result = rescale_to_unit([0.001, 0.002, 0.003])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

def test_rescale_unordered_list():
    result = rescale_to_unit([5.0, 1.0, 3.0, 2.0, 4.0])
    expected = [1.0, 0.0, 0.5, 0.25, 0.75]
    assert result == expected

def test_rescale_with_zero():
    result = rescale_to_unit([0.0, 10.0, 20.0])
    expected = [0.0, 0.5, 1.0]
    assert result == expected

def test_rescale_floating_point_precision():
    result = rescale_to_unit([1.1, 2.2, 3.3])
    expected = [0.0, 0.5, 1.0]
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

@pytest.mark.parametrize("numbers,expected", [
    ([0.0, 1.0], [0.0, 1.0]),
    ([10.0, 20.0, 30.0], [0.0, 0.5, 1.0]),
    ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0])
])
def test_rescale_parametrized(numbers, expected):
    result = rescale_to_unit(numbers)
    assert result == expected

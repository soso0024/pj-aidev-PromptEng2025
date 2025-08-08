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
import math


def test_basic_rescaling():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    min_number = min(numbers)
    max_number = max(numbers)
    if min_number == max_number:
        raise ValueError("All numbers are identical")
    return [(x - min_number) / (max_number - min_number) for x in numbers]


def test_single_value():
    with pytest.raises(ValueError):
        rescale_to_unit([5.0])


def test_same_values():
    with pytest.raises(ValueError):
        rescale_to_unit([2.0, 2.0, 2.0])


def test_negative_numbers():
    assert rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]


@pytest.mark.parametrize("input_list,expected", [
    ([0.0, 5.0, 10.0], [0.0, 0.5, 1.0]),
    ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0]),
    ([1.5, 2.5, 3.5], [0.0, 0.5, 1.0]),
    ([100.0, 200.0, 300.0], [0.0, 0.5, 1.0])
])
def test_various_ranges(input_list, expected):
    assert rescale_to_unit(input_list) == expected


def test_floating_point_precision():
    result = rescale_to_unit([0.1, 0.2, 0.3])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(a - b) < 1e-10 for a, b in zip(result, expected))


@pytest.mark.parametrize("invalid_input", [
    [],
    [None],
    ["1.0", "2.0"],
    ["1", "2", "3"]
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        rescale_to_unit(invalid_input)


def test_large_numbers():
    result = rescale_to_unit([1e6, 2e6, 3e6])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(a - b) < 1e-10 for a, b in zip(result, expected))


def test_small_numbers():
    result = rescale_to_unit([1e-6, 2e-6, 3e-6])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(a - b) < 1e-10 for a, b in zip(result, expected))


def test_mixed_positive_negative():
    result = rescale_to_unit([-5.5, 0.0, 5.5])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(a - b) < 1e-10 for a, b in zip(result, expected))
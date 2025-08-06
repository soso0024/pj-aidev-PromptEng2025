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
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_negative_numbers():
    assert rescale_to_unit([-2.0, -1.0, 0.0, 1.0, 2.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_same_numbers():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([1.0, 1.0, 1.0])


def test_two_numbers():
    assert rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]


@pytest.mark.parametrize("input_list,expected", [
    ([0.0, 5.0, 10.0], [0.0, 0.5, 1.0]),
    ([3.14, 2.718, 1.414, 1.732], [1.0, 0.7555040556199304, 0.0, 0.1840830449826989]),
    ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0]),
    ([1.0, 2.0], [0.0, 1.0])
])
def test_various_inputs(input_list, expected):
    result = rescale_to_unit(input_list)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)


def test_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])


def test_single_element():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([1.0])


def test_float_precision():
    result = rescale_to_unit([1.23456, 2.34567, 3.45678])
    expected = [0.0, 0.5, 1.0]
    assert all(math.isclose(r, e, rel_tol=1e-9) for r, e in zip(result, expected))


def test_large_numbers():
    result = rescale_to_unit([1e6, 2e6, 3e6])
    expected = [0.0, 0.5, 1.0]
    assert all(math.isclose(r, e, rel_tol=1e-9) for r, e in zip(result, expected))


def test_small_numbers():
    result = rescale_to_unit([1e-6, 2e-6, 3e-6])
    expected = [0.0, 0.5, 1.0]
    assert all(math.isclose(r, e, rel_tol=1e-9) for r, e in zip(result, expected))


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        raise ValueError("List cannot be empty")
    if len(numbers) == 1:
        raise ZeroDivisionError("List must contain at least two numbers")
    min_number = min(numbers)
    max_number = max(numbers)
    if min_number == max_number:
        raise ZeroDivisionError("All numbers in list are identical")
    return [(x - min_number) / (max_number - min_number) for x in numbers]
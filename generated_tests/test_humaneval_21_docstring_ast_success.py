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


def test_basic_rescale():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0] * len(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


@pytest.mark.parametrize("input_list,expected", [
    ([0.0, 10.0], [0.0, 1.0]),
    ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0]),
    ([1.0, 1.0, 1.0], [0.0, 0.0, 0.0]),
    ([2.5, 5.0, 7.5, 10.0], [0.0, 1/3, 2/3, 1.0]),
    ([-5.0, 0.0, 5.0, 10.0, 15.0], [0.0, 0.25, 0.5, 0.75, 1.0]),
])
def test_rescale_parametrized(input_list, expected):
    if len(set(input_list)) == 1:
        assert all(x == 0.0 for x in rescale_to_unit(input_list))
        return
    result = rescale_to_unit(input_list)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-10


def test_floating_point_precision():
    result = rescale_to_unit([0.1, 0.2, 0.3])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))


def test_negative_numbers():
    assert rescale_to_unit([-10.0, -5.0]) == [0.0, 1.0]


def test_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])


def test_single_element():
    with pytest.raises(ValueError):
        rescale_to_unit([1.0])


def test_large_numbers():
    result = rescale_to_unit([1e6, 2e6, 3e6])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))


def test_small_numbers():
    result = rescale_to_unit([1e-6, 2e-6, 3e-6])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))


def test_mixed_positive_negative():
    result = rescale_to_unit([-1.5, 0.0, 1.5])
    expected = [0.0, 0.5, 1.0]
    assert all(abs(r - e) < 1e-10 for r, e in zip(result, expected))
# Test cases for HumanEval/9
# Generated using Claude API

from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


# Generated test cases:
import pytest
from typing import List


def test_rolling_max_basic():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_empty():
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    assert rolling_max([5]) == [5]


@pytest.mark.parametrize("input_list,expected", [
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([1, 5, 2, 8, 3], [1, 5, 5, 8, 8]),
    ([-1, -2, -3, -4], [-1, -1, -1, -1]),
    ([0, 0, 0, 1, 0], [0, 0, 0, 1, 1]),
    ([10], [10]),
    ([1, 2], [1, 2]),
])
def test_rolling_max_various_inputs(input_list, expected):
    assert rolling_max(input_list) == expected


def test_rolling_max_negative_numbers():
    assert rolling_max([-5, -4, -6, -3, -7]) == [-5, -4, -4, -3, -3]


def test_rolling_max_mixed_numbers():
    assert rolling_max([-2, 0, 3, -1, 2]) == [-2, 0, 3, 3, 3]


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
    [1, "2", 3],
    [1, None, 3],
    [1, [], 3],
])
def test_rolling_max_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        rolling_max(invalid_input)


def test_rolling_max_string_input():
    with pytest.raises((TypeError, AttributeError)):
        rolling_max("string")


def test_rolling_max_large_numbers():
    assert rolling_max([1000000, 999999, 1000001]) == [1000000, 1000000, 1000001]


def test_rolling_max_duplicate_max():
    assert rolling_max([5, 5, 5, 4, 5, 5]) == [5, 5, 5, 5, 5, 5]


def test_rolling_max_alternating():
    assert rolling_max([1, 3, 1, 3, 1, 3]) == [1, 3, 3, 3, 3, 3]


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)

    return result
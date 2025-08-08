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


@pytest.mark.parametrize("numbers,expected", [
    ([1], [1]),
    ([], []),
    ([5, 5, 5], [5, 5, 5]),
    ([3, 2, 1], [3, 3, 3]),
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], [-1, -1, -1]),
    ([0, 0, 0], [0, 0, 0]),
    ([10, 5, 8, 3, 15, 4], [10, 10, 10, 10, 15, 15]),
    ([-5, -3, -1, 0, 2], [-5, -3, -1, 0, 2]),
])
def test_rolling_max_parametrized(numbers, expected):
    assert rolling_max(numbers) == expected


def test_rolling_max_single_element():
    assert rolling_max([42]) == [42]


def test_rolling_max_empty_list():
    assert rolling_max([]) == []


def test_rolling_max_negative_numbers():
    assert rolling_max([-3, -2, -4, -1, -5]) == [-3, -2, -2, -1, -1]


def test_rolling_max_duplicate_numbers():
    assert rolling_max([1, 1, 1, 2, 2, 2]) == [1, 1, 1, 2, 2, 2]


def test_rolling_max_descending():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_rolling_max_ascending():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
    [1, "2", 3],
    [1, None, 3],
    [1, [], 3],
])
def test_rolling_max_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        rolling_max(invalid_input)
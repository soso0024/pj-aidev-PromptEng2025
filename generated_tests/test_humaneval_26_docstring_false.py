# Test cases for HumanEval/26
# Generated using Claude API

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


# Generated test cases:
import pytest
from typing import List


def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []


def test_remove_duplicates_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_remove_duplicates_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == []


def test_remove_duplicates_some_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]


def test_remove_duplicates_negative_numbers():
    assert remove_duplicates([-1, -2, -2, -3, -1]) == [-3]


def test_remove_duplicates_mixed_numbers():
    assert remove_duplicates([-1, 0, 0, 1, -1, 2]) == [1, 2]


@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 2, 4], [1, 3, 4]),
    ([1, 1, 1], []),
    ([1], [1]),
    ([], []),
    ([1, 2, 3, 3, 2, 1, 4, 5], [4, 5]),
    ([-1, -1, 2, 3, -2, 3], [2, -2])
])
def test_remove_duplicates_parametrized(input_list, expected):
    assert remove_duplicates(input_list) == expected


def test_remove_duplicates_large_numbers():
    assert remove_duplicates([1000000, 999999, 1000000, 999999]) == []


def test_remove_duplicates_single_element():
    assert remove_duplicates([42]) == [42]


def test_remove_duplicates_maintains_order():
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [4, 9, 2, 6]


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    3.14,
    (1, 2, 3),
])
def test_remove_duplicates_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        remove_duplicates(invalid_input)


def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]
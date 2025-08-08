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


def test_basic_list():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == []


@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [1]),
    ([1, 1, 2, 2, 3, 3], []),
    ([1, 2, 3, 1, 2, 3], []),
    ([1, 2, 3, 4, 3, 2, 1], [4]),
])
def test_multiple_cases(input_list, expected):
    assert remove_duplicates(input_list) == expected


def test_negative_numbers():
    assert remove_duplicates([-1, -2, -1, -3, -2]) == [-3]


def test_mixed_numbers():
    assert remove_duplicates([-1, 0, 1, 0, -1, 2]) == [1, 2]


def test_large_numbers():
    assert remove_duplicates([1000000, 999999, 1000000]) == [999999]


def test_single_element():
    assert remove_duplicates([42]) == [42]


def test_preserve_order():
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [4, 9, 2, 6]


@pytest.mark.parametrize("input_list", [
    None,
    42,
    3.14
])
def test_invalid_input_type(input_list):
    with pytest.raises(TypeError):
        remove_duplicates(input_list)


def test_string_input():
    result = remove_duplicates(list("string"))
    assert result == ['t', 'r', 'i', 'n', 'g']


def test_list_with_none():
    result = remove_duplicates([1, None, 2])
    assert result == [1, None, 2]


def test_list_with_mixed_types():
    result = remove_duplicates([1, "2", 3])
    assert result == [1, "2", 3]


def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]
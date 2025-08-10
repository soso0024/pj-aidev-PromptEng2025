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
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] == 1]

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]

def test_remove_duplicates_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3, 4, 4, 5], [1, 3, 5]),
    ([1, 1, 1, 1], []),
    ([-1, -1, 0, 0, 1, 1], [])
])
def test_remove_duplicates_parametrized(input_list, expected):
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_large_list():
    large_list = list(range(1000)) + list(range(1000))
    result = remove_duplicates(large_list)
    assert len(result) == len(set(range(1000)))

def test_remove_duplicates_type_preservation():
    input_list = [1, 2, 2, 3, 4, 4, 5]
    result = remove_duplicates(input_list)
    assert all(isinstance(x, int) for x in result)

def test_remove_duplicates_order_preservation():
    input_list = [3, 1, 2, 2, 4, 3, 5]
    result = remove_duplicates(input_list)
    assert result == [1, 4, 5]
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

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([1]) == [1]

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

@pytest.mark.parametrize("input,expected", [
    ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5, 1, 2, 3], [1, 2, 3, 4, 5]),
    ([1, 1, 1, 2, 2, 3, 3, 3], [1, 2, 3]),
    ([1, 2, 1, 3, 2, 4, 5], [1, 2, 3, 4, 5]),
])
def test_remove_duplicates_with_parametrize(input, expected):
    assert remove_duplicates(input) == expected

def test_remove_duplicates_with_negative_numbers():
    assert remove_duplicates([-1, -2, -1, -3, -2, -4, -5]) == [-1, -2, -3, -4, -5]

def test_remove_duplicates_with_zero():
    assert remove_duplicates([0, 1, 0, 2, 3, 0]) == [0, 1, 2, 3]
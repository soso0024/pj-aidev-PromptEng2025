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

def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

def test_remove_duplicates_normal_case():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

def test_remove_duplicates_all_unique():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    assert remove_duplicates([1, 1, 2, 2, 3, 3]) == []

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_multiple_duplicates():
    assert remove_duplicates([1, 1, 1, 2, 2, 3, 4, 4, 5]) == [3, 5]

def test_remove_duplicates_preserves_order():
    assert remove_duplicates([3, 1, 2, 1, 4, 3, 5]) == [2, 4, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 2, 4], [1, 3, 4]),
    ([1, 1, 1, 1], []),
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
])
def test_remove_duplicates_parametrized(input_list, expected):
    assert remove_duplicates(input_list) == expected

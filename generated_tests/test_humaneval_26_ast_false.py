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

@pytest.mark.parametrize("numbers,expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 2], [2]),
    ([1, 2, 2, 3, 3, 3], [1]),
    ([1, 2, 1, 2, 3], [3]),
    ([-1, -1, 0, 1, 1], [0]),
    ([999, 999], []),
    ([1, 2, 3, 3, 2, 1], []),
    ([0], [0]),
])
def test_remove_duplicates_parametrized(numbers: List[int], expected: List[int]):
    from remove_duplicates import remove_duplicates
    assert remove_duplicates(numbers) == expected

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([42]) == [42]

def test_remove_duplicates_all_unique():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_same():
    assert remove_duplicates([1, 1, 1, 1]) == []

def test_remove_duplicates_mixed_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1]

def test_remove_duplicates_negative_numbers():
    assert remove_duplicates([-2, -2, -1, 0, 1, 1]) == [-1, 0]

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
])
def test_remove_duplicates_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        remove_duplicates(invalid_input)
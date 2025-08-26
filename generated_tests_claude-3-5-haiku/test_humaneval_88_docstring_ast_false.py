# Test cases for HumanEval/88
# Generated using Claude API


def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


# Generated test cases:
import pytest

def sort_array(array):
    return [] if len(array) == 0 else sorted(array, reverse=(array[0]+array[-1]) % 2 == 0)

def test_sort_array_empty_list():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_ascending_case():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

def test_sort_array_descending_case():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

@pytest.mark.parametrize("input_array,expected", [
    ([], []),
    ([5], [5]),
    ([2, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5]),
    ([2, 4, 3, 0, 1, 5, 6], [6, 5, 4, 3, 2, 1, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([10, 5, 8, 12], [12, 10, 8, 5])
])
def test_sort_array_parametrized(input_array, expected):
    assert sort_array(input_array) == expected

def test_sort_array_original_array_unchanged():
    original = [2, 4, 3, 0, 1, 5, 6]
    sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5, 6]
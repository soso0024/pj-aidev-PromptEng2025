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

def test_sort_array_empty():
    assert sort_array([]) == []

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
    ([4, 2, 6, 1, 3, 5], [1, 2, 3, 4, 5, 6])
])
def test_sort_array_normal(input, expected):
    assert sort_array(input) == expected

def test_sort_array_reverse():
    assert sort_array([5, 3, 1, 4, 2]) == [5, 4, 3, 2, 1]

def test_sort_array_single_element():
    assert sort_array([42]) == [42]

def test_sort_array_negative_numbers():
    assert sort_array([-3, -1, -2]) == [-3, -2, -1]

def sort_array(array):
    return sorted(array, reverse=(sum([array[0], array[-1]])) % 2 == 0) if array else []
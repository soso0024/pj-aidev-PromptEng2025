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

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_even_numbers():
    assert sort_array([2, 4, 6, 8]) == [8, 6, 4, 2]

def test_sort_array_odd_numbers():
    assert sort_array([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_sort_array_mixed_numbers():
    assert sort_array([2, 5, 8, 1, 3]) == [8, 5, 3, 2, 1]

def test_sort_array_negative_numbers():
    assert sort_array([-2, -5, -8, -1, -3]) == [-1, -2, -3, -5, -8]

def test_sort_array_zero():
    assert sort_array([0]) == [0]

def test_sort_array_duplicate_numbers():
    assert sort_array([2, 2, 4, 4, 6, 6]) == [6, 6, 4, 4, 2, 2]

@pytest.mark.parametrize("input,expected", [
    ([2, 4, 6, 8], [8, 6, 4, 2]),
    ([1, 3, 5, 7], [1, 3, 5, 7]),
    ([-2, -5, -8, -1, -3], [-8, -5, -3, -2, -1]),
    ([0], [0]),
    ([2, 2, 4, 4, 6, 6], [6, 6, 4, 4, 2, 2])
])
def test_sort_array_parametrized(input, expected):
    assert sort_array(input) == expected
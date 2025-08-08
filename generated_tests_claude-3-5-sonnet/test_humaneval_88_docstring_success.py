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

def test_empty_array():
    assert sort_array([]) == []

def test_single_element():
    assert sort_array([5]) == [5]

def test_two_elements_odd_sum():
    assert sort_array([1, 2]) == [1, 2]

def test_two_elements_even_sum():
    assert sort_array([2, 2]) == [2, 2]

@pytest.mark.parametrize("input_array,expected", [
    ([2, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5]),
    ([2, 4, 3, 0, 1, 5, 6], [6, 5, 4, 3, 2, 1, 0]),
    ([1, 3, 5, 7, 9], [9, 7, 5, 3, 1]),
    ([10, 8, 6, 4, 2], [10, 8, 6, 4, 2]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1])
])
def test_array_sorting(input_array, expected):
    assert sort_array(input_array) == expected

def test_array_immutability():
    original = [2, 4, 3, 0, 1, 5]
    original_copy = original.copy()
    sort_array(original)
    assert original == original_copy

def test_array_with_duplicates():
    assert sort_array([1, 2, 2, 1, 3, 3]) == [3, 3, 2, 2, 1, 1]

def test_array_with_zero():
    assert sort_array([0, 1, 2, 3, 0]) == [3, 2, 1, 0, 0]

def test_large_numbers():
    assert sort_array([1000000, 999999]) == [999999, 1000000]

def test_sequential_numbers():
    assert sort_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverse_sequential():
    assert sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
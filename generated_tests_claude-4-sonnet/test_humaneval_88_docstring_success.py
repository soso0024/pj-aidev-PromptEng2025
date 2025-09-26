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
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 

def test_empty_array():
    assert sort_array([]) == []

def test_single_element():
    assert sort_array([5]) == [5]
    assert sort_array([0]) == [0]
    assert sort_array([100]) == [100]

def test_two_elements_odd_sum():
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([3, 4]) == [3, 4]
    assert sort_array([5, 0]) == [0, 5]

def test_two_elements_even_sum():
    assert sort_array([2, 2]) == [2, 2]
    assert sort_array([1, 3]) == [3, 1]
    assert sort_array([0, 6]) == [6, 0]

def test_multiple_elements_odd_sum_ascending():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert sort_array([10, 5, 8, 1]) == [1, 5, 8, 10]

def test_multiple_elements_even_sum_descending():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([1, 3, 2, 5]) == [5, 3, 2, 1]
    assert sort_array([0, 1, 2, 8]) == [8, 2, 1, 0]

def test_all_same_elements():
    assert sort_array([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert sort_array([0, 0, 0]) == [0, 0, 0]
    assert sort_array([5, 5]) == [5, 5]

def test_already_sorted_ascending():
    assert sort_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]

def test_already_sorted_descending():
    assert sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert sort_array([4, 3, 2, 1, 0]) == [4, 3, 2, 1, 0]

def test_with_zeros():
    assert sort_array([0, 5, 3, 0, 1]) == [0, 0, 1, 3, 5]
    assert sort_array([0, 0, 0, 2]) == [2, 0, 0, 0]

def test_large_numbers():
    assert sort_array([100, 50, 75, 25, 99]) == [25, 50, 75, 99, 100]
    assert sort_array([1000, 500, 750, 250, 998]) == [1000, 998, 750, 500, 250]

def test_original_array_unchanged():
    original = [3, 1, 4, 1, 5]
    result = sort_array(original)
    assert original == [3, 1, 4, 1, 5]
    assert result != original

@pytest.mark.parametrize("array,expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 2], [2, 2]),
    ([3, 1, 4], [1, 3, 4]),
    ([2, 1, 4], [4, 2, 1]),
    ([0, 5, 3, 0, 1], [0, 0, 1, 3, 5]),
    ([1, 0, 3, 5, 0], [0, 0, 1, 3, 5])
])
def test_parametrized_cases(array, expected):
    assert sort_array(array) == expected
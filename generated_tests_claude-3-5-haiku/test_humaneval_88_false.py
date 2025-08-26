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

def test_sort_array_empty_list():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_ascending_when_sum_even():
    assert sort_array([2, 1, 3, 4]) == [1, 2, 3, 4]

def test_sort_array_descending_when_sum_odd():
    assert sort_array([1, 3, 2, 4]) == [4, 3, 2, 1]

@pytest.mark.parametrize("input_array,expected", [
    ([10, 5, 3, 8], [3, 5, 8, 10]),
    ([7, 2, 9, 1], [9, 7, 2, 1]),
    ([-1, -3, 0, 2], [-3, -1, 0, 2]),
    ([100, 50, 75, 25], [25, 50, 75, 100])
])
def test_sort_array_multiple_scenarios(input_array, expected):
    assert sort_array(input_array) == expected

def test_sort_array_with_duplicates():
    assert sort_array([3, 3, 2, 1]) == [1, 2, 3, 3]
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

@pytest.mark.parametrize("input_array,expected", [
    ([], []),
    ([5], [5]),
    ([2, 4, 3, 0, 1, 5], [0, 1, 2, 3, 4, 5]),
    ([2, 4, 3, 0, 1, 5, 6], [6, 5, 4, 3, 2, 1, 0]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
])
def test_sort_array(input_array, expected):
    from collections import deque
    
    def sort_array(array):
        return [] if len(array) == 0 else sorted(array, reverse=(array[0]+array[-1]) % 2 == 0)
    
    assert sort_array(input_array) == expected

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
    assert sort_array([1]) == [1]

def test_two_elements_sum_even():
    assert sort_array([1, 3]) == [3, 1]

def test_two_elements_sum_odd():
    assert sort_array([1, 2]) == [1, 2]

@pytest.mark.parametrize("input_array,expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 3, 5, 2], [1, 2, 3, 5]),
    ([2, 4, 6, 8], [8, 6, 4, 2])
])
def test_multiple_elements(input_array, expected):
    assert sort_array(input_array) == expected

@pytest.mark.parametrize("input_array,expected", [
    ([-1, -3, 2, 4], [-3, -1, 2, 4]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-5, 5, -4, 4], [5, 4, -4, -5]),
    ([10, -10, 20, -20], [20, 10, -10, -20])
])
def test_with_negative_numbers(input_array, expected):
    assert sort_array(input_array) == expected

def test_large_array():
    input_array = list(range(100))
    result = sort_array(input_array)
    assert len(result) == len(input_array)
    assert set(result) == set(input_array)

def test_duplicate_numbers():
    assert sort_array([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert sort_array([2, 2, 1, 1]) == [2, 2, 1, 1]

@pytest.mark.parametrize("input_array", [
    [float('inf'), 1, 2, 3],
    [-float('inf'), 1, 2, 3],
    [float('nan'), 1, 2, 3]
])
def test_special_numbers(input_array):
    result = sort_array(input_array)
    assert len(result) == len(input_array)
    assert set(str(x) for x in result) == set(str(x) for x in input_array)
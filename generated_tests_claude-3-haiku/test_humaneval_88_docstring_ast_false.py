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
    return [] if len(array) == 0 else sorted(array, reverse=(sum(array[:1] + array[-1:]) % 2 == 0))

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_even_sum():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

def test_sort_array_odd_sum():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

@pytest.mark.parametrize("input,expected", [
    ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 0], [0, 1, 2, 3, 4, 5]),
    ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]),
    ([9, 8, 7, 6, 5, 4], [9, 8, 7, 6, 5, 4])
])
def test_sort_array_parametrized(input, expected):
    assert sort_array(input) == expected

def test_sort_array_negative_values():
    with pytest.raises(ValueError):
        sort_array([-1, 2, 3, 4, 5])

def test_sort_array_non_integer_values():
    with pytest.raises(TypeError):
        sort_array([1, 2, 3.0, 4, 5])
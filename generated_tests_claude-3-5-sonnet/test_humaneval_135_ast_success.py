# Test cases for HumanEval/135
# Generated using Claude API


def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind


# Generated test cases:
import pytest

def test_empty_array():
    assert can_arrange([]) == -1

def test_single_element():
    assert can_arrange([1]) == -1

def test_two_elements_ascending():
    assert can_arrange([1, 2]) == -1

def test_two_elements_descending():
    assert can_arrange([2, 1]) == 1

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3, 4, 5], -1),
    ([5, 4, 3, 2, 1], 4),
    ([1, 3, 2, 4, 5], 2),
    ([1, 2, 4, 3, 5], 3),
    ([1, 1, 1, 1, 1], -1),
    ([1, 2, 2, 2, 1], 4),
    ([3, 1, 2, 4, 5], 1),
    ([5, 1, 2, 3, 4], 1),
    ([1, 5, 2, 3, 4], 2),
])
def test_various_arrays(input_arr, expected):
    assert can_arrange(input_arr) == expected

def test_array_with_duplicates():
    assert can_arrange([2, 2, 2, 2, 1]) == 4

def test_array_with_negative_numbers():
    assert can_arrange([-5, -4, -3, -2, -1]) == -1
    assert can_arrange([-1, -2, -3, -4, -5]) == 4

def test_array_with_mixed_numbers():
    assert can_arrange([-1, 0, 1, -2, 3]) == 3

def test_large_numbers():
    assert can_arrange([1000000, 2000000, 1500000]) == 2

def test_alternating_sequence():
    assert can_arrange([1, 3, 2, 4, 3, 5, 4]) == 6
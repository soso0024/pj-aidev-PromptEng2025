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

def test_can_arrange_empty_list():
    assert can_arrange([]) == -1

def test_can_arrange_single_element():
    assert can_arrange([1]) == -1

def test_can_arrange_sorted_ascending():
    assert can_arrange([1, 2, 3, 4, 5]) == -1

def test_can_arrange_unsorted():
    assert can_arrange([1, 2, 4, 3, 5]) == 3

def test_can_arrange_descending():
    assert can_arrange([5, 4, 3, 2, 1]) == 1

def test_can_arrange_multiple_descending_points():
    assert can_arrange([3, 2, 1, 4, 5]) == 2
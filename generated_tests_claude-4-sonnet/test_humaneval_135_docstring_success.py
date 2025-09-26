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

def can_arrange(arr):
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

def test_can_arrange_example_1():
    assert can_arrange([1,2,4,3,5]) == 3

def test_can_arrange_example_2():
    assert can_arrange([1,2,3]) == -1

def test_can_arrange_empty_array():
    assert can_arrange([]) == -1

def test_can_arrange_single_element():
    assert can_arrange([5]) == -1

def test_can_arrange_two_elements_ascending():
    assert can_arrange([1,2]) == -1

def test_can_arrange_two_elements_descending():
    assert can_arrange([2,1]) == 1

def test_can_arrange_all_descending():
    assert can_arrange([5,4,3,2,1]) == 4

def test_can_arrange_all_ascending():
    assert can_arrange([1,2,3,4,5]) == -1

def test_can_arrange_multiple_violations():
    assert can_arrange([3,1,4,2,5]) == 3

def test_can_arrange_violation_at_beginning():
    assert can_arrange([2,1,3,4,5]) == 1

def test_can_arrange_violation_at_end():
    assert can_arrange([1,2,3,5,4]) == 4

def test_can_arrange_negative_numbers():
    assert can_arrange([-1,-2,0,1]) == 1

def test_can_arrange_mixed_positive_negative():
    assert can_arrange([-5,-3,-1,0,2,1]) == 5

def test_can_arrange_large_numbers():
    assert can_arrange([100,200,150,300]) == 2

@pytest.mark.parametrize("arr,expected", [
    ([1,3,2,4,5], 2),
    ([10,5,15,20], 1),
    ([1], -1),
    ([5,4], 1),
    ([1,2], -1),
    ([3,2,1], 2),
    ([1,2,3,4], -1)
])
def test_can_arrange_parametrized(arr, expected):
    assert can_arrange(arr) == expected

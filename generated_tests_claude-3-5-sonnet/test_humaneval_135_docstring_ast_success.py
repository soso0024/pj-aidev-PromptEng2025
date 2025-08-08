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

def test_basic_case():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1

def test_empty_array():
    assert can_arrange([]) == -1

def test_single_element():
    assert can_arrange([1]) == -1

@pytest.mark.parametrize("arr,expected", [
    ([5, 4, 3, 2, 1], 4),
    ([1, 3, 2, 4, 5], 2),
    ([1, 2, 3, 4, 5], -1),
    ([5, 1, 2, 3, 4], 1),
    ([1, 5, 2, 3, 4], 2),
])
def test_various_arrangements(arr, expected):
    assert can_arrange(arr) == expected

def test_large_numbers():
    assert can_arrange([1000, 2000, 1500]) == 2
    assert can_arrange([999999, 1000000, 999998]) == 2

def test_negative_numbers():
    assert can_arrange([-3, -2, -1]) == -1
    assert can_arrange([-1, -3, -2]) == 1

def test_mixed_numbers():
    assert can_arrange([-1, 0, -2, 1]) == 2
    assert can_arrange([-5, 0, 5, -10, 15]) == 3

def test_two_elements():
    assert can_arrange([1, 2]) == -1
    assert can_arrange([2, 1]) == 1

@pytest.mark.parametrize("arr,expected", [
    ([10], -1),
    ([1, 2, 3, 4, 3], 4),
    ([5, 4, 3, 2, 1, 0], 5),
    ([1, 1000, 500, 2000], 2),
])
def test_edge_cases(arr, expected):
    assert can_arrange(arr) == expected
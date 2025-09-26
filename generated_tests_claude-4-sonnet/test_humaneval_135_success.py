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

def test_empty_array():
    assert can_arrange([]) == -1

def test_single_element():
    assert can_arrange([5]) == -1

def test_sorted_ascending():
    assert can_arrange([1, 2, 3, 4, 5]) == -1

def test_sorted_descending():
    assert can_arrange([5, 4, 3, 2, 1]) == 4

def test_one_violation():
    assert can_arrange([1, 3, 2, 4, 5]) == 2

def test_multiple_violations():
    assert can_arrange([5, 1, 4, 2, 3]) == 3

def test_last_element_violation():
    assert can_arrange([1, 2, 3, 5, 4]) == 4

def test_first_violation():
    assert can_arrange([2, 1, 3, 4, 5]) == 1

def test_all_equal_elements():
    assert can_arrange([3, 3, 3, 3]) == -1

def test_two_elements_sorted():
    assert can_arrange([1, 2]) == -1

def test_two_elements_unsorted():
    assert can_arrange([2, 1]) == 1

def test_duplicate_elements_with_violation():
    assert can_arrange([1, 3, 2, 2, 4]) == 2

def test_negative_numbers():
    assert can_arrange([-1, -3, -2, 0, 1]) == 1

def test_mixed_positive_negative():
    assert can_arrange([-5, -2, 1, 0, 3]) == 3

def test_large_array_no_violation():
    assert can_arrange(list(range(100))) == -1

def test_large_array_with_violation():
    arr = list(range(100))
    arr[50], arr[51] = arr[51], arr[50]
    assert can_arrange(arr) == 51

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], -1),
    ([3, 2, 1], 2),
    ([1, 3, 2], 2),
    ([2, 1, 3], 1),
    ([1], -1),
    ([], -1),
    ([5, 5, 5], -1),
    ([1, 2, 1, 3], 2)
])
def test_parametrized_cases(arr, expected):
    assert can_arrange(arr) == expected
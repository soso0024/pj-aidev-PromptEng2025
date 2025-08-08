# Test cases for HumanEval/73
# Generated using Claude API


def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


# Generated test cases:
import pytest

def smallest_change(arr):
    if not arr:
        return 0
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    
    return ans

def test_smallest_change_symmetric_array():
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 1]) == 2

def test_smallest_change_odd_length():
    assert smallest_change([1, 2, 3, 4, 5]) == 2
    assert smallest_change([5, 4, 3, 4, 5]) == 1

def test_smallest_change_even_length():
    assert smallest_change([1, 2, 3, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 2, 1]) == 2

def test_smallest_change_single_element():
    assert smallest_change([1]) == 0

def test_smallest_change_two_elements():
    assert smallest_change([1, 2]) == 1
    assert smallest_change([1, 1]) == 0

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3, 2, 1], 0),
    ([1, 2, 3, 4, 1], 2),
    ([5, 4, 3, 4, 5], 1),
    ([1, 2, 3, 3, 2, 1], 0),
    ([1, 2, 3, 4, 2, 1], 2),
    ([1], 0),
    ([1, 2], 1),
    ([1, 1], 0)
])
def test_smallest_change_parametrized(arr, expected):
    assert smallest_change(arr) == expected

def test_smallest_change_empty_array():
    assert smallest_change([]) == 0
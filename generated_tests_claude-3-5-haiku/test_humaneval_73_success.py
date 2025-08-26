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

def test_smallest_change_empty_list():
    assert smallest_change([]) == 0

def test_smallest_change_single_element():
    assert smallest_change([5]) == 0

def test_smallest_change_symmetric_list():
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 1, 1, 1]) == 0

def test_smallest_change_asymmetric_list():
    assert smallest_change([1, 2, 3, 4, 5]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6]) == 3

def test_smallest_change_different_types():
    assert smallest_change([1, 'a', 2, 'a', 1]) == 0
    assert smallest_change([1, 'a', 2, 'b', 1]) == 1

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 4, 3, 2, 1], 2),
    ([1, 1, 2, 2, 1], 1),
    ([], 0),
    ([1], 0),
    ([1, 2], 1),
    ([1, 2, 3], 1)
])
def test_smallest_change_parametrized(input_list, expected):
    assert smallest_change(input_list) == expected

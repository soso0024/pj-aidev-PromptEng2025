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
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

def test_smallest_change_empty_array():
    assert smallest_change([]) == 0

def test_smallest_change_single_element():
    assert smallest_change([1]) == 0

def test_smallest_change_two_elements_same():
    assert smallest_change([1, 1]) == 0

def test_smallest_change_two_elements_different():
    assert smallest_change([1, 2]) == 1

def test_smallest_change_already_palindrome_odd():
    assert smallest_change([1, 2, 3, 2, 1]) == 0

def test_smallest_change_already_palindrome_even():
    assert smallest_change([1, 2, 2, 1]) == 0

def test_smallest_change_example_1():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4

def test_smallest_change_example_2():
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1

def test_smallest_change_all_different():
    assert smallest_change([1, 2, 3, 4]) == 2

def test_smallest_change_all_same():
    assert smallest_change([5, 5, 5, 5, 5]) == 0

def test_smallest_change_negative_numbers():
    assert smallest_change([-1, -2, -3, -2, -1]) == 0

def test_smallest_change_mixed_positive_negative():
    assert smallest_change([-1, 2, -3, 4, -3, 2, -1]) == 0

def test_smallest_change_mixed_positive_negative_not_palindrome():
    assert smallest_change([-1, 2, -3, 4, 5, 2, -1]) == 1

def test_smallest_change_zeros():
    assert smallest_change([0, 0, 0, 0]) == 0

def test_smallest_change_with_zeros():
    assert smallest_change([0, 1, 2, 1, 0]) == 0

def test_smallest_change_large_numbers():
    assert smallest_change([1000, 2000, 3000, 2000, 1000]) == 0

def test_smallest_change_one_mismatch():
    assert smallest_change([1, 2, 3, 4, 5]) == 2

def test_smallest_change_partial_palindrome():
    assert smallest_change([1, 2, 3, 3, 4, 1]) == 1

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3, 5, 4, 7, 9, 6], 4),
    ([1, 2, 3, 4, 3, 2, 2], 1),
    ([1, 2, 3, 2, 1], 0),
    ([], 0),
    ([42], 0),
    ([1, 1], 0),
    ([1, 2], 1),
    ([1, 2, 1], 0),
    ([1, 2, 3], 1),
    ([5, 4, 3, 2, 1], 2)
])
def test_smallest_change_parametrized(arr, expected):
    assert smallest_change(arr) == expected

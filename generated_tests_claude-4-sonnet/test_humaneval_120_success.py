# Test cases for HumanEval/120
# Generated using Claude API


def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """

    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


# Generated test cases:
import pytest

def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

def test_maximum_k_zero():
    assert maximum([1, 2, 3, 4, 5], 0) == []

def test_maximum_empty_array_k_zero():
    assert maximum([], 0) == []

def test_maximum_single_element():
    assert maximum([5], 1) == [5]

def test_maximum_k_equals_array_length():
    arr = [3, 1, 4, 1, 5]
    result = maximum(arr, 5)
    assert sorted(result) == [1, 1, 3, 4, 5]

def test_maximum_k_less_than_array_length():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = maximum(arr, 3)
    assert sorted(result) == [5, 6, 9]

def test_maximum_negative_numbers():
    arr = [-1, -5, -3, -2, -4]
    result = maximum(arr, 2)
    assert sorted(result) == [-2, -1]

def test_maximum_mixed_positive_negative():
    arr = [-2, 5, -1, 3, 0, 4]
    result = maximum(arr, 3)
    assert sorted(result) == [3, 4, 5]

def test_maximum_duplicate_values():
    arr = [2, 2, 2, 2, 2]
    result = maximum(arr, 3)
    assert result == [2, 2, 2]

def test_maximum_k_one():
    arr = [10, 5, 8, 3, 15, 2]
    result = maximum(arr, 1)
    assert result == [15]

def test_maximum_already_sorted():
    arr = [1, 2, 3, 4, 5]
    result = maximum(arr, 3)
    assert result == [3, 4, 5]

def test_maximum_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    result = maximum(arr, 2)
    assert sorted(result) == [4, 5]

def test_maximum_floating_point():
    arr = [1.5, 2.7, 0.3, 4.1, 3.9]
    result = maximum(arr, 2)
    assert sorted(result) == [3.9, 4.1]

def test_maximum_large_numbers():
    arr = [1000000, 999999, 1000001, 500000]
    result = maximum(arr, 2)
    assert sorted(result) == [1000000, 1000001]

def test_maximum_modifies_original_array():
    arr = [3, 1, 4, 1, 5]
    original_arr = arr.copy()
    maximum(arr, 2)
    assert arr != original_arr
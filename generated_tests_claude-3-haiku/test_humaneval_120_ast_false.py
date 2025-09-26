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

def test_maximum_empty_array():
    assert maximum([], 0) == []

def test_maximum_single_element():
    assert maximum([1], 1) == [1]

def test_maximum_multiple_elements():
    assert maximum([3, 1, 4, 1, 5, 9, 2, 6, 5], 3) == [9, 6, 5]

def test_maximum_k_greater_than_length():
    assert maximum([1, 2, 3], 5) == [3, 2, 1]

def test_maximum_negative_numbers():
    assert maximum([-3, -1, -4, -1, -5, -9, -2, -6, -5], 3) == [-1, -1, -2]

def test_maximum_duplicate_values():
    assert maximum([1, 1, 2, 2, 3, 3], 3) == [3, 3, 2]

def test_maximum_k_zero():
    assert maximum([1, 2, 3], 0) == []

def test_maximum_single_element_k_one():
    assert maximum([42], 1) == [42]

def test_maximum_raises_type_error():
    with pytest.raises(TypeError):
        maximum(1, 2)
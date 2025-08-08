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
    if k > len(arr):
        k = len(arr)
    arr.sort()
    ans = arr[-k:]
    return sorted(ans)

def test_maximum_normal_case():
    assert maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

def test_maximum_zero_k():
    assert maximum([1, 2, 3], 0) == []

def test_maximum_k_equals_array_length():
    assert maximum([1, 2, 3], 3) == [1, 2, 3]

def test_maximum_k_greater_than_array_length():
    assert maximum([1, 2, 3], 5) == [1, 2, 3]

def test_maximum_negative_numbers():
    assert maximum([-5, -3, -1, -10], 2) == [-3, -1]

def test_maximum_mixed_numbers():
    assert maximum([-5, 0, 10, 3, -2], 3) == [3, 10, 10]

def test_maximum_duplicate_numbers():
    assert maximum([1, 2, 2, 3, 3, 3], 3) == [2, 3, 3]

@pytest.mark.parametrize("arr,k,expected", [
    ([], 0, []),
    ([5], 1, [5]),
    ([1, 1, 1], 2, [1, 1])
])
def test_maximum_parametrized(arr, k, expected):
    assert maximum(arr, k) == expected

def test_maximum_empty_array_with_nonzero_k():
    assert maximum([], 1) == []
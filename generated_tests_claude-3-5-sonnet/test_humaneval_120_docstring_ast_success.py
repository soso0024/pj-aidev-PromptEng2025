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

def test_basic_functionality():
    assert maximum([1, 2, 3], 2) == [2, 3]
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]

@pytest.mark.parametrize("arr,k,expected", [
    ([1], 1, [1]),
    ([-1000, 1000], 2, [-1000, 1000]),
    ([1, 2, 3, 4, 5], 0, []),
    ([5, 5, 5, 5], 3, [5, 5, 5]),
    ([-3, 2, 1, 2, -1, -2, 1], 1, [2]),
    ([0], 0, []),
    ([1, 1, 1, 1, 1], 5, [1, 1, 1, 1, 1]),
])
def test_various_inputs(arr, k, expected):
    assert maximum(arr, k) == expected

def test_large_array():
    large_arr = list(range(1000))
    assert maximum(large_arr, 5) == [995, 996, 997, 998, 999]

def test_negative_numbers():
    arr = [-5, -4, -3, -2, -1]
    assert maximum(arr, 3) == [-3, -2, -1]

def test_duplicate_numbers():
    arr = [1, 1, 1, 2, 2, 3, 3, 3]
    assert maximum(arr, 4) == [2, 3, 3, 3]

def test_single_element_array():
    assert maximum([42], 1) == [42]

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    assert maximum(arr, 3) == [3, 4, 5]

def test_already_sorted_array():
    arr = [1, 2, 3, 4, 5]
    assert maximum(arr, 3) == [3, 4, 5]

def test_all_same_elements():
    arr = [7] * 10
    assert maximum(arr, 5) == [7, 7, 7, 7, 7]

def test_mixed_positive_negative():
    arr = [-5, 5, -4, 4, -3, 3]
    assert maximum(arr, 4) == [-3, 3, 4, 5]

def test_k_equals_array_length():
    arr = [1, 2, 3, 4]
    assert maximum(arr, 4) == [1, 2, 3, 4]
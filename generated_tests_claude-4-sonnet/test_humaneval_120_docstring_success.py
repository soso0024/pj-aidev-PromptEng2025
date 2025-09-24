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

def test_maximum_example_1():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]

def test_maximum_example_2():
    assert maximum([4, -4, 4], 2) == [4, 4]

def test_maximum_example_3():
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

def test_maximum_k_zero():
    assert maximum([1, 2, 3], 0) == []

def test_maximum_k_equals_array_length():
    assert maximum([1, 3, 2], 3) == [1, 2, 3]

def test_maximum_single_element():
    assert maximum([5], 1) == [5]

def test_maximum_all_negative():
    assert maximum([-5, -2, -8, -1], 2) == [-2, -1]

def test_maximum_all_positive():
    assert maximum([1, 5, 3, 9, 2], 3) == [3, 5, 9]

def test_maximum_duplicates():
    assert maximum([1, 1, 1, 1], 2) == [1, 1]

def test_maximum_mixed_values():
    assert maximum([-10, 0, 10, -5, 5], 3) == [0, 5, 10]

def test_maximum_boundary_values():
    assert maximum([-1000, 1000, 0], 2) == [0, 1000]

def test_maximum_large_array():
    arr = list(range(100, 0, -1))
    result = maximum(arr, 5)
    assert result == [96, 97, 98, 99, 100]

def test_maximum_k_one():
    assert maximum([3, 1, 4, 1, 5], 1) == [5]

@pytest.mark.parametrize("arr,k,expected", [
    ([1], 0, []),
    ([2, 1], 1, [2]),
    ([1, 2, 3], 2, [2, 3]),
    ([-1, -2, -3], 1, [-1]),
    ([0, 0, 0], 2, [0, 0])
])
def test_maximum_parametrized(arr, k, expected):
    assert maximum(arr, k) == expected

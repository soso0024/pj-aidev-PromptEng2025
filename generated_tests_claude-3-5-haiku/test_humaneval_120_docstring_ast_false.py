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
    return sorted(ans)

def test_maximum_normal_cases():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

def test_maximum_edge_cases():
    assert maximum([1], 1) == [1]
    assert maximum([1, 2, 3], 0) == []
    assert maximum([1, 2, 3], 3) == [1, 2, 3]

def test_maximum_duplicate_values():
    assert maximum([5, 5, 5, 5], 2) == [5, 5]

def test_maximum_negative_values():
    assert maximum([-1, -2, -3, -4], 2) == [-1, -2]

def test_maximum_mixed_values():
    assert maximum([-10, 0, 10, -5, 5], 3) == [0, 5, 10]

@pytest.mark.parametrize("arr,k,expected", [
    ([-3, -4, 5], 3, [-4, -3, 5]),
    ([4, -4, 4], 2, [4, 4]),
    ([-3, 2, 1, 2, -1, -2, 1], 1, [2]),
    ([1], 1, [1]),
    ([1, 2, 3], 0, []),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([5, 5, 5, 5], 2, [5, 5]),
    ([-1, -2, -3, -4], 2, [-1, -2]),
    ([-10, 0, 10, -5, 5], 3, [0, 5, 10])
])
def test_maximum_parametrized(arr, k, expected):
    assert maximum(arr, k) == expected
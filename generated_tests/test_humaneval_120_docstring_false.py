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

def test_maximum_basic():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
    ([5, 4, 3, 2, 1], 2, [4, 5]),
    ([-1000, 1000], 2, [-1000, 1000]),
    ([1], 1, [1]),
    ([1, 1, 1, 1], 2, [1, 1]),
    ([-5, -4, -3, -2, -1], 3, [-3, -2, -1]),
    ([0], 1, [0]),
    ([1, 2, 3], 0, []),
])
def test_maximum_parametrized(arr, k, expected):
    assert maximum(arr, k) == expected

def test_maximum_edge_cases():
    assert maximum([1], 0) == []
    assert maximum([1, 2, 3], 3) == [1, 2, 3]
    assert maximum([100], 1) == [100]

def test_maximum_duplicates():
    assert maximum([1, 1, 1, 1, 1], 3) == [1, 1, 1]
    assert maximum([3, 3, 3, 2, 2, 1, 1], 4) == [2, 2, 3, 3]

def test_maximum_negative_numbers():
    assert maximum([-5, -4, -3, -2, -1], 5) == [-5, -4, -3, -2, -1]
    assert maximum([-10, -20, -30], 2) == [-20, -10]

def test_maximum_mixed_numbers():
    assert maximum([-1, 0, 1], 3) == [-1, 0, 1]
    assert maximum([-100, 0, 100], 2) == [0, 100]

def test_maximum_invalid_inputs():
    test_cases = [
        ([1, 2, 3], -1),
        ([1, 2, 3], 4),
        ([], 1)
    ]
    for arr, k in test_cases:
        try:
            maximum(arr, k)
            assert False, f"Should have raised ValueError for arr={arr}, k={k}"
        except (ValueError, IndexError):
            pass
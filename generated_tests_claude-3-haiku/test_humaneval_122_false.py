# Test cases for HumanEval/122
# Generated using Claude API


def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


# Generated test cases:
from solution import add_elements
import pytest

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 3, 6),
    ([10, 20, 30, 40, 50], 2, 30),
    ([-1, -2, -3, -4, -5], 4, -6),
    ([0, 0, 0, 0, 0], 5, 0),
    ([], 0, 0),
    ([1, 10, 100, 1000, 10000], 3, 111),
    ([12, 34, 56, 78, 90], 5, 180),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
])
def test_add_elements(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_empty_array():
    assert add_elements([], 0) == 0

def test_add_elements_k_greater_than_length():
    with pytest.raises(IndexError):
        add_elements([1, 2, 3], 5)

def test_add_elements_negative_k():
    with pytest.raises(IndexError):
        add_elements([1, 2, 3], -1)
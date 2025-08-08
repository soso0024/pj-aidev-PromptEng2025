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
import pytest

def test_add_elements_empty_array():
    assert add_elements([], 2) == 0

def test_add_elements_single_element():
    assert add_elements([10], 1) == 10

def test_add_elements_multiple_elements():
    assert add_elements([12, 345, 6, 78], 3) == 18

def test_add_elements_all_elements_longer_than_2_digits():
    assert add_elements([123, 456, 789], 3) == 0

def test_add_elements_negative_k():
    with pytest.raises(IndexError):
        add_elements([1, 2, 3], -1)

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 3, 6),
    ([10, 20, 30, 40, 50], 2, 30),
    ([1, 12, 123, 1234, 12345], 4, 33),
    ([-1, -2, -3, -4, -5], 2, -3),
    ([0, 0, 0, 0, 0], 5, 0)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected
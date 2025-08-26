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
    assert add_elements([10, 20, 300, 4], 3) == 34

def test_add_elements_all_elements_longer_than_2_digits():
    assert add_elements([123, 456, 789], 3) == 0

def test_add_elements_negative_numbers():
    assert add_elements([-10, -20, -3, 4], 4) == -29

def test_add_elements_k_greater_than_array_length():
    assert add_elements([10, 20, 30], 5) == 60

@pytest.mark.parametrize("arr,k,expected", [
    ([10, 20, 300, 4], 3, 34),
    ([123, 456, 789], 3, 0),
    ([-10, -20, -3, 4], 4, -29),
    ([10, 20, 30], 5, 60),
    ([], 2, 0),
    ([10], 1, 10)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected
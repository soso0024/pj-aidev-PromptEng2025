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

def test_add_elements_normal_case():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    assert add_elements(arr, k) == 24

def test_add_elements_all_single_digit():
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert add_elements(arr, k) == 15

def test_add_elements_no_valid_elements():
    arr = [1000, 2000, 3000]
    k = 3
    assert add_elements(arr, k) == 0

def test_add_elements_mixed_elements():
    arr = [10, 200, 3, 4000, 50]
    k = 4
    assert add_elements(arr, k) == 213

def test_add_elements_k_less_than_array_length():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 2
    assert add_elements(arr, k) == 24

@pytest.mark.parametrize("arr,k,expected", [
    ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4, 24),
    ([1, 2, 3, 4, 5], 5, 15),
    ([1000, 2000, 3000], 3, 0),
    ([10, 200, 3, 4000, 50], 4, 213),
    ([99, 100, 101, 102], 3, 199)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_single_element_array():
    arr = [42]
    k = 1
    assert add_elements(arr, k) == 42

def test_add_elements_zero_element():
    arr = [0, 1, 2]
    k = 3
    assert add_elements(arr, k) == 3
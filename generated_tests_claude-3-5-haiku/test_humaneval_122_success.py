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
    assert add_elements([10, 20, 30, 40], 3) == 60

def test_add_elements_empty_array():
    assert add_elements([], 2) == 0

def test_add_elements_fewer_elements_than_k():
    assert add_elements([5, 15], 3) == 20

def test_add_elements_with_multi_digit_numbers():
    assert add_elements([100, 20, 30, 40], 3) == 50

def test_add_elements_with_single_digit_numbers():
    assert add_elements([1, 2, 3, 4, 5], 4) == 10

@pytest.mark.parametrize("arr,k,expected", [
    ([10, 20, 30, 40], 2, 30),
    ([5, 15, 25, 35], 3, 45),
    ([1, 22, 333, 4444], 4, 23),
    ([], 0, 0)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_with_zero_k():
    assert add_elements([10, 20, 30], 0) == 0

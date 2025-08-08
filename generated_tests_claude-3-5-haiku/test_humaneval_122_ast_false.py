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

def add_elements(arr, k):
    return sum(int(elem) for elem in arr[:k] if len(str(abs(int(elem)))) <= 2)

def test_add_elements_normal_case():
    assert add_elements([1, 2, 3, 4, 5], 3) == 6
    assert add_elements([10, 20, 30, 40, 50], 2) == 30

def test_add_elements_with_single_digit():
    assert add_elements([1, 22, 333, 4444], 3) == 23

def test_add_elements_empty_array():
    assert add_elements([], 5) == 0

def test_add_elements_k_larger_than_array():
    assert add_elements([1, 2, 3], 5) == 6

def test_add_elements_with_mixed_types():
    assert add_elements([1, '22', 333, '4'], 3) == 354

@pytest.mark.parametrize("arr,k,expected", [
    ([10, 20, 30, 40, 50], 3, 60),
    ([1, 22, 333, 4444], 2, 23),
    ([], 5, 0),
    ([100, 200, 300], 5, 600),
    ([1, '22', 333, '4'], 3, 354)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_with_large_numbers():
    assert add_elements([1000, 2000, 3000], 2) == 0

def test_add_elements_with_negative_numbers():
    assert add_elements([-10, -22, -333, -4444], 3) == -32
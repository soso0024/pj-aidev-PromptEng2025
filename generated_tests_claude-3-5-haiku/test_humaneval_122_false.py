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
    assert add_elements([1, 2, 3, 4, 5], 3) == 6
    assert add_elements([10, 20, 30, 40, 50], 2) == 30

def test_add_elements_with_two_digit_numbers():
    assert add_elements([10, 20, 30, 100, 200], 3) == 60

def test_add_elements_with_three_digit_numbers():
    assert add_elements([100, 200, 300, 10, 20], 3) == 30

def test_add_elements_empty_array():
    assert add_elements([], 5) == 0

def test_add_elements_k_larger_than_array():
    assert add_elements([1, 2, 3], 5) == 6

@pytest.mark.parametrize("arr,k,expected", [
    ([1, 2, 3, 4, 5], 3, 6),
    ([10, 20, 30, 40, 50], 2, 30),
    ([100, 200, 10, 20, 30], 3, 30),
    ([], 5, 0),
    ([1000, 2000, 30, 40, 50], 4, 70)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected
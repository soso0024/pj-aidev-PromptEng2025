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
    assert add_elements([], 5) == 0

def test_add_elements_less_than_k():
    assert add_elements([5, 15, 25], 5) == 45

def test_add_elements_with_single_digit():
    assert add_elements([5, 15, 100, 200], 3) == 20

def test_add_elements_with_three_digit_numbers():
    assert add_elements([5, 15, 100, 200, 300], 4) == 20

def test_add_elements_mixed_numbers():
    assert add_elements([5, 15, 100, 200, 300, 10], 6) == 30

@pytest.mark.parametrize("arr,k,expected", [
    ([10, 20, 30, 40], 3, 60),
    ([], 5, 0),
    ([5, 15, 25], 5, 45),
    ([5, 15, 100, 200], 3, 20),
    ([5, 15, 100, 200, 300], 4, 20),
    ([5, 15, 100, 200, 300, 10], 6, 30)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_negative_numbers():
    assert add_elements([-10, -20, -30, 40], 3) == -30

def test_add_elements_zero_k():
    assert add_elements([10, 20, 30], 0) == 0
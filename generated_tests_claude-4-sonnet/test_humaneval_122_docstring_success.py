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
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

def test_example_case():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24

def test_single_element():
    assert add_elements([5], 1) == 5

def test_single_element_three_digits():
    assert add_elements([111], 1) == 0

def test_all_single_digits():
    assert add_elements([1, 2, 3, 4, 5], 3) == 6

def test_all_two_digits():
    assert add_elements([10, 20, 30, 40], 2) == 30

def test_all_three_digits():
    assert add_elements([100, 200, 300], 3) == 0

def test_mixed_digits():
    assert add_elements([1, 22, 333, 4, 55], 5) == 82

def test_k_equals_array_length():
    assert add_elements([1, 2, 3], 3) == 6

def test_negative_single_digit():
    assert add_elements([-5, 10, 20], 3) == 25

def test_negative_two_digits():
    assert add_elements([-15, 25, 100], 2) == 25

def test_negative_three_digits():
    assert add_elements([-100, 5, 10], 3) == 15

def test_zero():
    assert add_elements([0, 1, 2], 3) == 3

def test_large_numbers():
    assert add_elements([1000, 2000, 5, 10], 4) == 15

def test_k_is_one():
    assert add_elements([99, 100, 200], 1) == 99

def test_k_is_one_three_digits():
    assert add_elements([100, 99, 88], 1) == 0

def test_mixed_with_zero():
    assert add_elements([0, 100, 50, 5], 4) == 55

@pytest.mark.parametrize("arr,k,expected", [
    ([1, 2, 3, 4, 5], 1, 1),
    ([10, 20, 30], 2, 30),
    ([100, 200], 1, 0),
    ([99, 100, 1], 3, 100),
    ([1, 11, 111, 1111], 4, 12),
    ([-1, -11, -111], 3, -1),
    ([0], 1, 0),
    ([12, 34, 56, 78, 90], 5, 270)
])
def test_parametrized_cases(arr, k, expected):
    assert add_elements(arr, k) == expected
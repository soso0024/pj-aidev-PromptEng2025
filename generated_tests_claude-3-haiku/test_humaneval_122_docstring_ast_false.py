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
    assert add_elements([], 1) == 0

def test_add_elements_single_element():
    assert add_elements([12], 1) == 12
    assert add_elements([9], 1) == 9

def test_add_elements_multiple_elements():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 15
    assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90], 3) == 60

def test_add_elements_k_greater_than_length():
    assert add_elements([1, 2, 3], 5) == 6

def test_add_elements_negative_numbers():
    assert add_elements([-11, -2, -3, -4, -5], 5) == -25

def test_add_elements_zero():
    assert add_elements([0, 0, 0, 0, 0], 5) == 0

@pytest.mark.parametrize("arr,k,expected", [
    ([], 0, 0),
    ([1], 1, 1),
    ([11, 22, 33, 44, 55], 3, 66),
    ([100, 200, 300, 400, 500], 2, 300),
    ([-1, -2, -3, -4, -5], 3, -6),
    ([0, 0, 0, 0, 0], 5, 0)
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_invalid_input():
    with pytest.raises(TypeError):
        add_elements(None, 1)
    with pytest.raises(TypeError):
        add_elements([1, 2, 3], None)
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
    result = add_elements([], 1)
    assert result == 0

def test_add_elements_k_zero():
    result = add_elements([1, 2, 3], 1)
    assert result == 1

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 3, 6),
    ([10, 20, 30, 40, 50], 5, 150),
    ([9, 99, 999, 9999], 4, 108),
    ([1, 2, 1000, 3, 4], 5, 10),
    ([11, 22, 33], 2, 33),
])
def test_add_elements_normal_cases(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_k_larger_than_array():
    assert add_elements([1, 2, 3], 5) == 6

def test_add_elements_all_large_numbers():
    assert add_elements([100, 200, 1000, 2000], 3) == 300

def test_add_elements_mixed_numbers():
    assert add_elements([5, 15, 100, 25, 999], 4) == 45

def test_add_elements_single_element():
    assert add_elements([7], 1) == 7

@pytest.mark.parametrize("arr, k, expected", [
    ([11, 22, 33, 44], 2, 33),
    ([99, 100, 101, 102], 3, 99),
    ([1, 22, 333, 4444], 4, 23),
])
def test_add_elements_boundary_cases(arr, k, expected):
    assert add_elements(arr, k) == expected

@pytest.mark.parametrize("arr, k", [
    (None, 3),
    ("not_an_array", 2),
    ([1, 2, 3], "not_a_number"),
])
def test_add_elements_invalid_inputs(arr, k):
    with pytest.raises((TypeError)):
        add_elements(arr, k)

def test_add_elements_negative_k():
    result = add_elements([1, 2, 3], -1)
    assert result == 0
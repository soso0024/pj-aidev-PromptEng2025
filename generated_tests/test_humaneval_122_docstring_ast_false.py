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

def test_basic_functionality():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([1, 2, 3, 4, 5], 3) == 6

@pytest.mark.parametrize("arr, k, expected", [
    ([10, 20, 30, 40, 50], 3, 60),
    ([99, 999, 99, 999], 4, 198),
    ([1], 1, 1),
    ([10, 20], 2, 30),
    ([1000, 2000, 3], 3, 3),
    ([11, 22, 33, 44, 55], 5, 165),
    ([9, 99, 999, 9999], 4, 108),
])
def test_various_inputs(arr, k, expected):
    assert add_elements(arr, k) == expected

@pytest.mark.parametrize("arr, k", [
    ([], 1),
    ([1, 2, 3], 0),
    ([1, 2], 3),
])
def test_invalid_inputs(arr, k):
    with pytest.raises(IndexError):
        add_elements(arr, k)

def test_edge_cases():
    assert add_elements([10, 99, 98], 1) == 10
    assert add_elements([1000, 100, 10], 3) == 10
    assert add_elements([99, 99, 99], 3) == 297

def test_all_large_numbers():
    assert add_elements([1000, 2000, 3000], 3) == 0

def test_mixed_numbers():
    assert add_elements([1, 10, 1000, 10, 10000], 5) == 21

def test_single_digit_numbers():
    assert add_elements([1, 2, 3, 4, 5], 5) == 15

def test_exactly_two_digits():
    assert add_elements([10, 20, 30, 40, 50], 5) == 150

def test_k_equals_one():
    assert add_elements([99, 1000, 2000], 1) == 99

def test_all_numbers_qualify():
    assert add_elements([10, 20, 30], 3) == 60
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

def test_add_elements_basic():
    assert add_elements([1, 2, 3, 4, 5], 3) == 6
    assert add_elements([10, 20, 30], 2) == 30

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3], 3, 6),
    ([10, 20, 100, 200], 2, 30),
    ([99, 100, 200, 300], 4, 99),
    ([1], 1, 1),
    ([1000, 2000], 2, 0),
    ([1, 2], 2, 3),
    ([1], 1, 1),
    ([100, 2, 3], 1, 0),
])
def test_add_elements_parametrized(arr, k, expected):
    assert add_elements(arr, k) == expected

def test_add_elements_empty_array():
    result = add_elements([], 1)
    assert result == 0

def test_add_elements_k_zero():
    result = add_elements([1, 2, 3], 0)
    assert result == 0

def test_add_elements_negative_numbers():
    assert add_elements([-1, -2, -3], 2) == -3

@pytest.mark.parametrize("arr, k", [
    (None, 1),
    ("invalid", 1),
    ([1, 2, 3], "invalid"),
])
def test_add_elements_invalid_inputs(arr, k):
    with pytest.raises((TypeError, ValueError)):
        add_elements(arr, k)

def test_add_elements_negative_k():
    result = add_elements([1, 2, 3], -1)
    assert result == 0

def test_add_elements_large_numbers():
    assert add_elements([1000, 1, 2, 3], 4) == 6

def test_add_elements_mixed_numbers():
    assert add_elements([99, 100, 5, 1000, 2], 5) == 106

def test_add_elements_decimal_numbers():
    result = add_elements([1.5, 2.7, 3.2], 3)
    assert result == 7.4
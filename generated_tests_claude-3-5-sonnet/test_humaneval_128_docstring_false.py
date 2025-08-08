# Test cases for HumanEval/128
# Generated using Claude API


def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


# Generated test cases:
import pytest

def test_empty_array():
    assert prod_signs([]) is None

def test_single_positive():
    assert prod_signs([1]) == 1

def test_single_negative():
    assert prod_signs([-1]) == -1

def test_single_zero():
    assert prod_signs([0]) == 0

def test_all_positive():
    assert prod_signs([1, 2, 3]) == 6

def test_all_negative():
    assert prod_signs([-1, -2, -3]) == -6

def test_mixed_signs():
    assert prod_signs([1, -2, 3, -4]) == 10

def test_with_zero():
    assert prod_signs([1, -2, 0, 3]) == 0

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 2, -4], -9),
    ([0, 1], 0),
    ([-1, -2, -3, -4], -10),
    ([1, 1, 1, 1], 4),
    ([0, 0, 0], 0),
    ([1, -1], -2),
    ([100, -100], -200),
    ([1, 2, -3, 0, 4], 0),
    ([-1], -1),
    ([1], 1),
    ([0], 0)
])
def test_prod_signs_parametrized(input_arr, expected):
    assert prod_signs(input_arr) == expected

def test_large_numbers():
    assert prod_signs([1000000, -1000000]) == -2000000

def test_multiple_zeros():
    assert prod_signs([0, 1, 0, -1, 0]) == 0

def test_alternating_signs():
    assert prod_signs([1, -1, 1, -1, 1]) == -5

def test_same_magnitude_different_signs():
    assert prod_signs([5, -5, 5, -5]) == 20
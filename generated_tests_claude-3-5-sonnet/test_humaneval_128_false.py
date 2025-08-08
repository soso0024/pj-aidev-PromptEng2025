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

def test_prod_signs_empty_array():
    assert prod_signs([]) is None

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([1, -2, 3], -6),
    ([0], 0),
    ([1, 0, -1], 0),
    ([-1], -1),
    ([1], 1),
    ([1, -1], -2),
    ([-2, -3, -4], -9),
    ([2, -3, 4, -5], 14),
    ([10], 10),
    ([-10], -10),
    ([1, 2, 3, 4, 5], 15),
    ([-1, -2, -3, -4, -5], -15),
    ([0, 0, 0], 0),
    ([1, -1, 0], 0),
    ([100, -200, 300], -600),
    ([0.5, -1.5, 2.5], -4.5),
    ([1, -1, 1, -1], 4),
    ([2, 2, -2, -2], 8)
])
def test_prod_signs_various_inputs(arr, expected):
    assert prod_signs(arr) == expected

def test_prod_signs_single_zero():
    assert prod_signs([0]) == 0

def test_prod_signs_with_zeros():
    assert prod_signs([1, 0, 2, 0, 3]) == 0

def test_prod_signs_all_positive():
    assert prod_signs([1, 2, 3, 4]) == 10

def test_prod_signs_all_negative():
    assert prod_signs([-1, -2, -3, -4]) == 10

def test_prod_signs_mixed_signs():
    assert prod_signs([1, -2, 3, -4]) == -10

def test_prod_signs_single_element():
    assert prod_signs([42]) == 42
    assert prod_signs([-42]) == -42

def test_prod_signs_two_elements():
    assert prod_signs([10, -10]) == -20

def test_prod_signs_large_numbers():
    assert prod_signs([1000, -2000, 3000]) == -6000
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
from solution import prod_signs
import pytest

@pytest.mark.parametrize("arr,expected", [
    ([], None),
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([0, 1, 2], 0),
    ([0, -1, 2], 0),
    ([-1, 0, 2], 0),
    ([1, -2, 3], -6),
    ([-1, 2, -3], 6),
    ([0, 0, 0], 0),
    ([1, -1, 1, -1], 0),
    ([1, 1, 1, 1], 4),
    ([-1, -1, -1, -1], -4),
])
def test_prod_signs(arr, expected):
    assert prod_signs(arr) == expected

def test_prod_signs_empty_input():
    assert prod_signs([]) is None

def test_prod_signs_all_zeros():
    assert prod_signs([0, 0, 0]) == 0

def test_prod_signs_mixed_signs():
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, 2, -3]) == 6

def test_prod_signs_all_positive():
    assert prod_signs([1, 1, 1, 1]) == 4

def test_prod_signs_all_negative():
    assert prod_signs([-1, -1, -1, -1]) == -4
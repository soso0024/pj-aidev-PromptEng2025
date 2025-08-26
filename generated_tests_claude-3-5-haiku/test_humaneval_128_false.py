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

def test_prod_signs_empty_list():
    assert prod_signs([]) is None

def test_prod_signs_zero_in_list():
    assert prod_signs([1, 2, 0, 3]) == 0
    assert prod_signs([0]) == 0

def test_prod_signs_positive_list():
    assert prod_signs([1, 2, 3, 4]) == 10
    assert prod_signs([5, 7]) == 12

def test_prod_signs_negative_list():
    assert prod_signs([-1, -2, -3]) == 6
    assert prod_signs([-5, -7]) == 12

def test_prod_signs_mixed_signs():
    assert prod_signs([-1, 2, -3, 4]) == -10
    assert prod_signs([1, -2, 3, -4]) == -10

@pytest.mark.parametrize("input_list,expected", [
    ([], None),
    ([0], 0),
    ([1, 2, 0, 3], 0),
    ([1, 2, 3, 4], 10),
    ([-1, -2, -3], 6),
    ([-1, 2, -3, 4], -10),
    ([5, 7], 12),
    ([-5, -7], 12)
])
def test_prod_signs_parametrized(input_list, expected):
    assert prod_signs(input_list) == expected
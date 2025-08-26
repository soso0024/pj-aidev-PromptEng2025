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
from prod_signs import prod_signs
import pytest

def test_prod_signs_empty_list():
    assert prod_signs([]) is None

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([1, -2, 3], -6),
    ([0, 2, 3], 0),
    ([0, -2, 3], 0),
    ([0, 0, 0], 0)
])
def test_prod_signs_normal_cases(input_list, expected):
    assert prod_signs(input_list) == expected
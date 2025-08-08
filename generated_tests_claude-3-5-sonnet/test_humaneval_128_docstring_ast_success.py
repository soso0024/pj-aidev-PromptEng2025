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
import math

def test_empty_array():
    assert prod_signs([]) is None

def test_single_positive():
    assert prod_signs([1]) == 1

def test_single_negative():
    assert prod_signs([-1]) == -1

def test_single_zero():
    assert prod_signs([0]) == 0

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 2, -4], -9),
    ([0, 1], 0),
    ([1, -1, -1, 1], 4),
    ([-1, -2, -3], -6),
    ([1, 2, 3], 6),
    ([0, 0, 0], 0),
    ([1, 0, -1], 0),
    ([-10, 5, -2], 17),
    ([100, -100], -200),
    ([1, 1, 1, -1], -4),
])
def test_prod_signs_various_cases(input_arr, expected):
    assert prod_signs(input_arr) == expected

@pytest.mark.parametrize("input_arr", [
    [1, 2, float('inf')],
    [float('nan'), 1, 2],
    [float('-inf'), 3, 4]
])
def test_prod_signs_with_special_floats(input_arr):
    result = prod_signs(input_arr)
    assert math.isinf(result) or math.isnan(result)

def test_large_numbers():
    assert prod_signs([1000000, -1000000, 1000000]) == -3000000

def test_small_numbers():
    assert prod_signs([-0.1, -0.2, -0.3]) == -0.6

def test_mixed_numbers():
    assert prod_signs([1.5, -2.5, 3.5]) == -7.5
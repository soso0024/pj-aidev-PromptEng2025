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

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([1, -2, 3], -6),
    ([0], 0),
    ([1, 0, -1], 0),
    ([-1], -1),
    ([1], 1),
    ([1, -1], -2),
    ([10, -10], -20),
    ([-2, -3, -4], -9),
    ([2, 3, 4], 9),
    ([1, -2, 3, -4], 10),
    ([0, 0, 0], 0),
    ([1, 2, 3, 0, 4], 0),
    ([-1, -1, -1, -1], 4),
    ([100], 100),
    ([-100], -100),
    ([1, -1, 0, 2], 0)
])
def test_prod_signs_various_inputs(input_arr, expected):
    assert prod_signs(input_arr) == expected

@pytest.mark.parametrize("input_arr", [
    [1.5, 2.5],
    [-1.5, -2.5],
    [1.5, -2.5],
    [0.0, 1.5]
])
def test_prod_signs_float_inputs(input_arr):
    result = prod_signs(input_arr)
    assert isinstance(result, float)

def test_single_zero():
    assert prod_signs([0]) == 0

def test_large_numbers():
    assert prod_signs([1000000, -1000000]) == -2000000

def test_mixed_types():
    assert prod_signs([1, -2.5, 3, -4.5]) == 11.0

@pytest.mark.parametrize("invalid_input", [
    "string",
    123,
    True
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        prod_signs(invalid_input)

def test_none_input():
    with pytest.raises((TypeError, AttributeError)):
        prod_signs(None)

def test_bool_input():
    with pytest.raises((TypeError, AttributeError)):
        prod_signs(False)
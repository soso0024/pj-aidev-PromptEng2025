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

def prod_signs(arr):
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

def test_empty_array():
    assert prod_signs([]) is None

def test_array_with_zero():
    assert prod_signs([0, 1]) == 0
    assert prod_signs([1, 0, 2]) == 0
    assert prod_signs([0]) == 0
    assert prod_signs([-1, 0, 2]) == 0

def test_all_positive():
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([5]) == 5
    assert prod_signs([1, 1, 1, 1]) == 4

def test_all_negative():
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([-5]) == -5
    assert prod_signs([-1, -1]) == 2

def test_mixed_positive_negative():
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([-1, 2, 3]) == -6
    assert prod_signs([1, -2, 3, -4]) == 10
    assert prod_signs([-1, -2, 3]) == 6

def test_single_element():
    assert prod_signs([5]) == 5
    assert prod_signs([-5]) == -5
    assert prod_signs([0]) == 0

def test_even_number_of_negatives():
    assert prod_signs([-1, -2]) == 3
    assert prod_signs([-1, -2, -3, -4]) == 10

def test_odd_number_of_negatives():
    assert prod_signs([-1]) == -1
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([-1, 2, -3, 4, -5]) == -15

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 2, -4], -9),
    ([0, 1], 0),
    ([], None),
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([0], 0),
    ([-1, 2, 3], -6),
    ([1, -2, 3, -4], 10),
    ([-5], -5),
    ([5], 5)
])
def test_parametrized_cases(arr, expected):
    assert prod_signs(arr) == expected

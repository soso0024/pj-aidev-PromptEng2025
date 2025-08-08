# Test cases for HumanEval/116
# Generated using Claude API


def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


# Generated test cases:
from functools import cmp_to_key

def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(abs(x))[2:].count('1'), x))

import pytest

@pytest.mark.parametrize("arr,expected", [
    ([5, 3, 2, 1, 4], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([], []),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1]),
    ([-1, 0, 1], [-1, 0, 1]),
    ([10, 5, 15], [5, 10, 15]),
    ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
    ([0b101, 0b1010, 0b11], [0b1010, 0b101, 0b11])
])
def test_sort_array(arr, expected):
    assert sort_array(arr) == expected

@pytest.mark.parametrize("arr", [
    None,
    "test",
    [1, 2, "3"],
    [1.0, 2.0, 3.0]
])
def test_sort_array_invalid_input(arr):
    with pytest.raises(TypeError):
        sort_array(arr)
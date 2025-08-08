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
from your_module import sort_array

import pytest

@pytest.mark.parametrize("arr,expected", [
    ([1, 5, 2, 3, 4], [1, 2, 3, 4, 5]),
    ([-2, -3, -4, -5, -6], [-6, -5, -4, -3, -2]),
    ([1, 0, 2, 3, 4], [0, 1, 2, 3, 4]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([], []),
    ([1], [1]),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([10, 5, 15, 20, 25], [5, 10, 15, 20, 25]),
    ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
    ([1, 1, 2, 2, 2], [1, 1, 2, 2, 2]),
    ([2, 2, 2, 1, 1], [1, 1, 2, 2, 2]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([0, 0, 0, 0, 1], [0, 0, 0, 0, 1]),
    ([1, 0, 0, 0, 0], [0, 0, 0, 0, 1]),
    ([1, 1, 1, 1, 0], [0, 1, 1, 1, 1]),
    ([0, 0, 0, 1, 1], [0, 0, 0, 1, 1]),
    ([1, 1, 0, 0, 0], [0, 0, 0, 1, 1]),
])
def test_sort_array(arr, expected):
    assert sort_array(arr) == expected
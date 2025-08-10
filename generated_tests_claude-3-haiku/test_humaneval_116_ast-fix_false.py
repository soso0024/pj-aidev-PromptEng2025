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
import pytest

def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(abs(x))[2:].count('1'), x))

def test_sort_array(arr, expected):
    assert sort_array(arr) == expected

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([42]) == [42]

def test_sort_array_negative_numbers():
    assert sort_array([-5, -3, -1, 0, 1, 3, 5]) == [-1, 0, 1, -3, -5, 3, 5]

def test_sort_array_duplicate_values():
    assert sort_array([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]

def test_sort_array_raises_error_on_non_iterable():
    with pytest.raises(TypeError):
        sort_array(42)
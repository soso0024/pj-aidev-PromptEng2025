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
import pytest

def test_sort_array_positive_numbers():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]

def test_sort_array_zero_and_positive():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]

def test_sort_array_negative_numbers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]

def test_sort_array_mixed_numbers():
    assert sort_array([-1, 0, 1, 2, 3]) == [-1, 0, 1, 2, 3]
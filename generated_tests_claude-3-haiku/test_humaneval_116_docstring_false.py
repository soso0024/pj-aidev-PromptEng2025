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

def test_sort_array_positive_integers():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert sort_array([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_array_negative_integers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    assert sort_array([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]
    assert sort_array([-5, -4, -3, -2, -1]) == [-5, -4, -3, -2, -1]

def test_sort_array_mixed_integers():
    assert sort_array([-1, 0, 1, -2, 2]) == [-2, -1, 0, 1, 2]
    assert sort_array([1, -1, 2, -2, 3]) == [-2, -1, 1, 2, 3]
    assert sort_array([0, -1, 1, -2, 2]) == [-2, -1, 0, 1, 2]

def test_sort_array_empty_list():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([42]) == [42]

def test_sort_array_duplicate_elements():
    assert sort_array([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
    assert sort_array([0, 0, 1, 1, 1]) == [0, 0, 1, 1, 1]
    assert sort_array([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

def test_sort_array_large_input():
    large_input = [i for i in range(1000)]
    large_expected = sorted(sorted(large_input), key=lambda x: bin(x)[2:].count('1'))
    assert sort_array(large_input) == large_expected
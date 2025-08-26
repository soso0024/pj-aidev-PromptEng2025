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

def test_sort_array_empty_list():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_already_sorted():
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_array_reverse_sorted():
    assert sort_array([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_array_with_duplicates():
    assert sort_array([3, 1, 4, 1, 5, 2]) == [1, 1, 2, 3, 4, 5]

def test_sort_array_with_negative_numbers():
    assert sort_array([-3, 1, -4, 1, -5, 2]) == [-5, -4, -3, 1, 1, 2]

def test_sort_array_with_zero():
    assert sort_array([0, 1, 0, 3, 12]) == [0, 0, 1, 3, 12]

@pytest.mark.parametrize("input,expected", [
    ([3, 1, 4, 1, 5, 2], [1, 1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([-3, 1, -4, 1, -5, 2], [-5, -4, -3, 1, 1, 2]),
    ([0, 1, 0, 3, 12], [0, 0, 1, 3, 12]),
    ([], [])
])
def test_sort_array_parametrized(input, expected):
    assert sort_array(input) == expected

def sort_array(arr):
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
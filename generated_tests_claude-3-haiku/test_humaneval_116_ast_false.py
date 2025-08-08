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

@pytest.mark.parametrize("arr, expected", [
    ([5, 3, 2, 1, 4], [1, 2, 3, 4, 5]),
    ([0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1]),
    ([-2, 1, -1, 2, 3, 0], [-2, -1, 0, 1, 2, 3]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([], []),
    ([42], [42]),
])
def test_sort_array(arr, expected):
    def sort_array(arr):
        return sorted(sorted(arr), key=lambda x: bin(abs(x))[2:].count('1'))
    assert sort_array(arr) == expected

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([42]) == [42]

def test_sort_array_negative_numbers():
    assert sort_array([-2, 1, -1, 2, 3, 0]) == [-2, -1, 0, 1, 2, 3]

def test_sort_array_duplicate_numbers():
    assert sort_array([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
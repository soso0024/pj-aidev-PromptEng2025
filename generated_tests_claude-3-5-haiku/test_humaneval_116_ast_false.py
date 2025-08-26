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

def test_sort_array_multiple_elements():
    assert sort_array([3, 1, 2, 4]) == [1, 2, 4, 3]

def test_sort_array_with_negative_numbers():
    assert sort_array([-3, -1, 0, 2, 4]) == [-1, 0, 2, -3, 4]

def test_sort_array_with_duplicates():
    assert sort_array([7, 7, 5, 5, 3, 3]) == [5, 5, 3, 3, 7, 7]

@pytest.mark.parametrize("input_arr,expected", [
    ([7, 6, 15, 8], [6, 7, 8, 15]),
    ([1024, 512, 256, 128], [128, 256, 512, 1024]),
    ([100, 50, 25, 12], [50, 12, 25, 100])
])
def test_sort_array_parametrized(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_sort_array_large_numbers():
    assert sort_array([1000000, 500000, 250000]) == [500000, 250000, 1000000]

def test_sort_array_zero_and_positive():
    assert sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]
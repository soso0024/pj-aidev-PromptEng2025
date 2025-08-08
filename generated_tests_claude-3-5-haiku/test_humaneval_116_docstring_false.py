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

def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(abs(x))[2:].count('1'), x))

def test_sort_array_normal_case():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]

def test_sort_array_negative_numbers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]

def test_sort_array_zero_and_positive():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]

def test_sort_array_same_binary_ones():
    assert sort_array([3, 5, 7]) == [3, 5, 7]

def test_sort_array_empty_list():
    assert sort_array([]) == []

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 5, 2, 3, 4], [1, 2, 3, 4, 5]),
    ([-2, -3, -4, -5, -6], [-6, -5, -4, -3, -2]),
    ([1, 0, 2, 3, 4], [0, 1, 2, 3, 4]),
    ([3, 5, 7], [3, 5, 7]),
    ([], [])
])
def test_sort_array_parametrized(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_sort_array_large_numbers():
    assert sort_array([1024, 512, 256, 128]) == [128, 256, 512, 1024]

def test_sort_array_mixed_numbers():
    assert sort_array([15, 7, 3, 1, 0]) == [0, 1, 3, 7, 15]
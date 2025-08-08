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

def test_empty_array():
    assert sort_array([]) == []

def test_single_element():
    assert sort_array([1]) == [1]

def test_basic_positive_numbers():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

def test_with_zero():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

def test_negative_numbers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

def test_mixed_numbers():
    assert sort_array([-1, 0, 1, -2, 2]) == [0, -2, -1, 1, 2]

@pytest.mark.parametrize("input_arr,expected", [
    ([7, 6, 15, 8], [8, 6, 7, 15]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 4, 8, 3, 5, 6, 9, 7]),
    ([10, 20, 30, 40], [10, 20, 40, 30]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
])
def test_various_arrays(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_large_numbers():
    assert sort_array([1024, 512, 256, 128]) == [128, 256, 512, 1024]

def test_powers_of_two():
    assert sort_array([16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16]

def test_same_number_of_ones():
    assert sort_array([3, 5, 6, 9]) == [3, 5, 6, 9]

def test_duplicate_numbers():
    assert sort_array([3, 3, 3, 3]) == [3, 3, 3, 3]

def test_mixed_duplicates():
    assert sort_array([7, 8, 7, 8]) == [8, 8, 7, 7]
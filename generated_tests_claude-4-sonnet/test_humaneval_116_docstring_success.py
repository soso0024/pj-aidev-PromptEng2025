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
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

def test_sort_array_basic_case():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]

def test_sort_array_negative_numbers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]

def test_sort_array_with_zero():
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_all_zeros():
    assert sort_array([0, 0, 0]) == [0, 0, 0]

def test_sort_array_same_bit_count():
    assert sort_array([3, 5, 6]) == [3, 5, 6]

def test_sort_array_powers_of_two():
    assert sort_array([8, 4, 2, 1, 16]) == [1, 2, 4, 8, 16]

def test_sort_array_mixed_positive_negative():
    assert sort_array([1, -1, 2, -2]) == [-2, -1, 1, 2]

def test_sort_array_large_numbers():
    assert sort_array([255, 256, 127]) == [256, 127, 255]

@pytest.mark.parametrize("input_arr,expected", [
    ([0], [0]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([7, 8], [8, 7]),
    ([15, 16], [16, 15]),
    ([3, 6, 9, 12], [3, 6, 9, 12])
])
def test_sort_array_parametrized(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_sort_array_duplicate_values():
    assert sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]

def test_sort_array_reverse_sorted():
    assert sort_array([5, 4, 3, 2, 1]) == [1, 2, 4, 3, 5]

def test_sort_array_already_sorted():
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]
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
    ([1, 2, 4, 8, 16, 32], [1, 2, 4, 8, 16, 32]),
    ([31, 15, 7, 3, 1], [1, 3, 7, 15, 31]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1024, 512, 256, 128], [128, 256, 512, 1024])
])
def test_parametrized_cases(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_large_numbers():
    assert sort_array([1000000, 1000001, 1000002]) == [1000000, 1000001, 1000002]

def test_duplicate_numbers():
    assert sort_array([3, 3, 3, 3]) == [3, 3, 3, 3]

def test_binary_edge_cases():
    assert sort_array([2, 3, 5, 7, 11, 13, 17, 19]) == [2, 3, 5, 17, 7, 11, 13, 19]

def test_mixed_binary_weights():
    assert sort_array([10, 21, 42, 84]) == [10, 21, 42, 84]
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

def test_same_number_of_ones():
    assert sort_array([3, 5]) == [3, 5]

def test_different_number_of_ones():
    assert sort_array([7, 8]) == [8, 7]

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3, 4], [1, 2, 4, 3]),
    ([3, 7, 8, 9], [8, 3, 9, 7]),
    ([1024, 512, 256, 128], [128, 256, 512, 1024]),
    ([15, 7, 3, 1], [1, 3, 7, 15]),
])
def test_various_arrays(input_arr, expected):
    assert sort_array(input_arr) == expected

@pytest.mark.parametrize("input_arr,expected", [
    ([0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1]),
    ([2, 2, 2], [2, 2, 2]),
])
def test_identical_elements(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_large_numbers():
    assert sort_array([1000000, 1048576, 2097152]) == [1048576, 2097152, 1000000]

def test_powers_of_two():
    assert sort_array([16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16]

def test_all_ones():
    assert sort_array([15, 31, 7, 3]) == [3, 7, 15, 31]

def test_zero_and_powers_of_two():
    assert sort_array([0, 1, 2, 4, 8]) == [0, 1, 2, 4, 8]

@pytest.mark.parametrize("input_arr", [
    None,
    "string",
    123,
    3.14
])
def test_invalid_input_type(input_arr):
    with pytest.raises((TypeError, AttributeError)):
        sort_array(input_arr)

def test_array_with_negative_numbers():
    result = sort_array([-1, -2, -3])
    assert result == [-2, -1, -3]
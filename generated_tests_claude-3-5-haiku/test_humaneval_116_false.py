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

def test_sort_array_basic():
    assert sort_array([3, 1, 2, 4]) == [1, 2, 3, 4]

def test_sort_array_with_bit_count():
    assert sort_array([7, 6, 15, 8]) == [8, 6, 7, 15]

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_negative_numbers():
    assert sort_array([-3, -1, -2, -4]) == [-4, -3, -2, -1]

def test_sort_array_mixed_numbers():
    assert sort_array([-1, 0, 3, -5, 7]) == [0, -1, -5, 3, 7]

@pytest.mark.parametrize("input_arr,expected", [
    ([3, 1, 2, 4], [1, 2, 3, 4]),
    ([7, 6, 15, 8], [8, 6, 7, 15]),
    ([], []),
    ([5], [5]),
    ([-3, -1, -2, -4], [-4, -3, -2, -1]),
    ([-1, 0, 3, -5, 7], [0, -1, -5, 3, 7])
])
def test_sort_array_parametrized(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_sort_array_type_error():
    with pytest.raises(TypeError):
        sort_array(None)

def test_sort_array_non_numeric():
    with pytest.raises(TypeError):
        sort_array(['a', 'b', 'c'])
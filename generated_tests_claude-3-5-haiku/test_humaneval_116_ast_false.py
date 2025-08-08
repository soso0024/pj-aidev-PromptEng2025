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
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    for item in arr:
        if not isinstance(item, (int, float)):
            raise TypeError("List must contain only numbers")
    
    return sorted(arr, key=lambda x: (bin(abs(x))[2:].count('1'), x))

def test_sort_array_empty_list():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_multiple_elements():
    assert sort_array([3, 1, 2, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_array_with_negative_numbers():
    assert sort_array([-3, -1, 2, 4, -5]) == [-1, -3, -5, 2, 4]

def test_sort_array_with_zero():
    assert sort_array([0, 1, 2, 3]) == [0, 1, 2, 3]

@pytest.mark.parametrize("input_arr,expected", [
    ([7, 6, 15, 8], [8, 6, 15, 7]),
    ([2, 4, 8, 16], [2, 4, 8, 16]),
    ([1024, 512, 256, 128], [128, 256, 512, 1024])
])
def test_sort_array_parametrized(input_arr, expected):
    assert sort_array(input_arr) == expected

def test_sort_array_large_numbers():
    assert sort_array([1000000, 500000, 250000]) == [250000, 500000, 1000000]

def test_sort_array_duplicate_numbers():
    assert sort_array([3, 3, 1, 2, 2]) == [1, 2, 2, 3, 3]

def test_sort_array_type_error():
    with pytest.raises(TypeError):
        sort_array("not a list")

def test_sort_array_mixed_types():
    with pytest.raises(TypeError):
        sort_array([1, "string", 3.14])
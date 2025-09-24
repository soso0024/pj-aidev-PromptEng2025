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

class TestSortArray:
    
    def test_empty_array(self):
        assert sort_array([]) == []
    
    def test_single_element(self):
        assert sort_array([5]) == [5]
    
    def test_two_elements_same_bit_count(self):
        assert sort_array([3, 5]) == [3, 5]
    
    def test_two_elements_different_bit_count(self):
        assert sort_array([1, 2]) == [1, 2]
    
    def test_multiple_elements_ascending_bit_count(self):
        assert sort_array([1, 2, 4]) == [1, 2, 4]
    
    def test_multiple_elements_descending_bit_count(self):
        assert sort_array([4, 2, 1]) == [1, 2, 4]
    
    def test_same_bit_count_sorted_by_value(self):
        assert sort_array([3, 5, 6, 9, 10, 12]) == [3, 5, 6, 9, 10, 12]
    
    def test_mixed_bit_counts(self):
        assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    
    def test_zero_included(self):
        assert sort_array([0, 1, 2]) == [0, 1, 2]
    
    def test_only_zeros(self):
        assert sort_array([0, 0, 0]) == [0, 0, 0]
    
    def test_large_numbers(self):
        assert sort_array([15, 7, 3, 1]) == [1, 3, 7, 15]
    
    def test_powers_of_two(self):
        assert sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]
    
    def test_duplicate_values(self):
        assert sort_array([3, 3, 5, 5]) == [3, 3, 5, 5]
    
    def test_complex_case(self):
        assert sort_array([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4, 8, 3, 5, 6, 7]
    
    @pytest.mark.parametrize("input_arr,expected", [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([0], [0]),
        ([7, 3], [3, 7]),
        ([8, 4, 2, 1, 16], [1, 2, 4, 8, 16]),
        ([15, 14, 13, 12], [12, 13, 14, 15])
    ])
    def test_parametrized_cases(self, input_arr, expected):
        assert sort_array(input_arr) == expected
    
    def test_negative_numbers(self):
        result = sort_array([-1, 2, 3])
        assert isinstance(result, list)
    
    def test_non_integer_raises_error(self):
        with pytest.raises(TypeError):
            sort_array([1.5, 2, 3])
    
    def test_string_in_array_raises_error(self):
        with pytest.raises(TypeError):
            sort_array([1, "2", 3])
    
    def test_none_in_array_raises_error(self):
        with pytest.raises(TypeError):
            sort_array([1, None, 3])
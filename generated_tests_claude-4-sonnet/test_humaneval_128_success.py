# Test cases for HumanEval/128
# Generated using Claude API


def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


# Generated test cases:
import pytest

def prod_signs(arr):
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

class TestProdSigns:
    
    def test_empty_array(self):
        assert prod_signs([]) is None
    
    def test_none_input(self):
        assert prod_signs(None) is None
    
    def test_single_positive(self):
        assert prod_signs([5]) == 5
    
    def test_single_negative(self):
        assert prod_signs([-5]) == -5
    
    def test_single_zero(self):
        assert prod_signs([0]) == 0
    
    def test_all_positive(self):
        assert prod_signs([1, 2, 3, 4]) == 10
    
    def test_all_negative_even_count(self):
        assert prod_signs([-1, -2, -3, -4]) == 10
    
    def test_all_negative_odd_count(self):
        assert prod_signs([-1, -2, -3]) == -6
    
    def test_mixed_positive_negative_even_negatives(self):
        assert prod_signs([1, -2, 3, -4]) == 10
    
    def test_mixed_positive_negative_odd_negatives(self):
        assert prod_signs([1, -2, 3]) == -6
    
    def test_contains_zero(self):
        assert prod_signs([1, 2, 0, 4]) == 0
    
    def test_contains_zero_with_negatives(self):
        assert prod_signs([-1, 2, 0, -4]) == 0
    
    def test_multiple_zeros(self):
        assert prod_signs([0, 0, 0]) == 0
    
    def test_large_numbers(self):
        assert prod_signs([100, -200, 300]) == -600
    
    def test_decimal_numbers(self):
        assert prod_signs([1.5, -2.5, 3.5]) == -7.5
    
    @pytest.mark.parametrize("arr,expected", [
        ([1], 1),
        ([-1], -1),
        ([1, 2], 3),
        ([-1, -2], 3),
        ([-1, 2], -3),
        ([1, -2], -3),
        ([1, 2, 3], 6),
        ([-1, -2, -3], -6),
        ([1, -2, -3], 6),
        ([-1, 2, -3], 6),
        ([-1, -2, 3], 6),
        ([1, 2, -3], -6)
    ])
    def test_parametrized_cases(self, arr, expected):
        assert prod_signs(arr) == expected
    
    def test_very_large_array(self):
        arr = [1] * 1000 + [-1] * 500
        expected = 1500
        assert prod_signs(arr) == expected
    
    def test_alternating_signs(self):
        arr = [1, -1, 2, -2, 3, -3]
        expected = -12
        assert prod_signs(arr) == expected
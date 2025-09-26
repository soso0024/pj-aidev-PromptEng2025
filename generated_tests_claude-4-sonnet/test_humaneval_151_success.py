# Test cases for HumanEval/151
# Generated using Claude API


def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])


# Generated test cases:
import pytest

def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

class TestDoubleTheDifference:
    
    def test_empty_list(self):
        assert double_the_difference([]) == 0
    
    def test_single_positive_odd_integer(self):
        assert double_the_difference([3]) == 9
    
    def test_single_positive_even_integer(self):
        assert double_the_difference([4]) == 0
    
    def test_single_negative_odd_integer(self):
        assert double_the_difference([-3]) == 0
    
    def test_single_zero(self):
        assert double_the_difference([0]) == 0
    
    def test_single_positive_float(self):
        assert double_the_difference([3.5]) == 0
    
    def test_single_negative_float(self):
        assert double_the_difference([-3.5]) == 0
    
    def test_multiple_positive_odd_integers(self):
        assert double_the_difference([1, 3, 5]) == 1 + 9 + 25
    
    def test_multiple_positive_even_integers(self):
        assert double_the_difference([2, 4, 6]) == 0
    
    def test_mixed_positive_integers(self):
        assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25
    
    def test_mixed_positive_negative_integers(self):
        assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25
    
    def test_all_negative_integers(self):
        assert double_the_difference([-1, -3, -5]) == 0
    
    def test_floats_only(self):
        assert double_the_difference([1.5, 2.5, 3.5]) == 0
    
    def test_mixed_integers_and_floats(self):
        assert double_the_difference([1, 2.5, 3, 4.5, 5]) == 1 + 9 + 25
    
    def test_large_numbers(self):
        assert double_the_difference([101, 103]) == 101**2 + 103**2
    
    def test_single_one(self):
        assert double_the_difference([1]) == 1
    
    def test_zeros_and_ones(self):
        assert double_the_difference([0, 1, 0, 1]) == 2
    
    def test_negative_zero_positive_mix(self):
        assert double_the_difference([-5, 0, 5]) == 25
    
    def test_decimal_strings_as_floats(self):
        assert double_the_difference([1.0, 3.0, 5.0]) == 0
    
    def test_very_large_odd_number(self):
        assert double_the_difference([999]) == 999**2
    
    def test_alternating_signs(self):
        assert double_the_difference([1, -1, 3, -3, 5, -5]) == 1 + 9 + 25

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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_single_odd_positive():
    assert double_the_difference([1]) == 1
    assert double_the_difference([3]) == 9
    assert double_the_difference([5]) == 25

def test_single_even_positive():
    assert double_the_difference([2]) == 0
    assert double_the_difference([4]) == 0

def test_single_negative():
    assert double_the_difference([-1]) == 0
    assert double_the_difference([-3]) == 0
    assert double_the_difference([-2]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_single_float():
    assert double_the_difference([1.5]) == 0
    assert double_the_difference([3.0]) == 0
    assert double_the_difference([2.5]) == 0

def test_mixed_integers():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_with_negatives():
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([-1, 3, -5, 7]) == 58

def test_with_floats():
    assert double_the_difference([1.0, 3, 5.5, 7]) == 58
    assert double_the_difference([2.5, 4.7, 6.1]) == 0
    assert double_the_difference([1.1, 3.3, 5.5]) == 0

def test_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5, -7]) == 0

def test_all_floats():
    assert double_the_difference([1.5, 2.7, 3.9]) == 0

def test_large_numbers():
    assert double_the_difference([11, 13, 15]) == 121 + 169 + 225

def test_mixed_types():
    assert double_the_difference([1, 2.0, 3, 4.5, 5]) == 35

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
    ([1], 1),
    ([2], 0),
    ([-1], 0),
    ([1.5], 0),
    ([1, 3, 5, 7, 9], 165),
    ([2, 4, 6, 8, 10], 0),
    ([-1, -3, -5], 0),
    ([1.0, 3.0, 5.0], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 165)
])
def test_parametrized_cases(input_list, expected):
    assert double_the_difference(input_list) == expected

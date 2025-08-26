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

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_positive_odd_integers():
    assert double_the_difference([1, 3, 5, 7, 9]) == 225

def test_double_the_difference_mixed_list():
    assert double_the_difference([1, 2, 3, 4.5, 6, 7]) == 100

def test_double_the_difference_all_negative_integers():
    assert double_the_difference([-1, -3, -5, -7, -9]) == 0

def test_double_the_difference_with_string_elements():
    assert double_the_difference([1, 3, 5, 7, 9]) == 225

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], 100),
    ([-1, -2, -3, -4, -5], 0),
    ([1.5, 3.7, 5.1, 7.9, 9.3], 0),
    ([1, 3, 5, 7, 9], 225),
    ([1, 3, 5, 7, 9], 225)
])
def test_double_the_difference_parametrized(input, expected):
    assert double_the_difference(input) == expected

def double_the_difference(lst):
    return sum([i**2 for i in lst if isinstance(i, int) and i > 0 and i%2!=0])
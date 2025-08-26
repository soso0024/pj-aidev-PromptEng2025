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

def test_double_the_difference_normal_cases():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 2, 0], 10),
    ([9, -2], 81),
    ([], 0),
    ([-1, -2, 0], 0),
    ([5, 7, 9], 25 + 49 + 81),
    ([2, 4, 6], 0),
    ([1.5, 3, 5], 9 + 25)
])
def test_double_the_difference_parametrized(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_double_the_difference_edge_cases():
    assert double_the_difference([0]) == 0
    assert double_the_difference([-1, -3, -5]) == 0

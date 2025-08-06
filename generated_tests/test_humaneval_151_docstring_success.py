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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_no_odd_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_floating_point_numbers():
    assert double_the_difference([1.5, 2.5, 3.5]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 2, 0], 10),
    ([9, -2], 81),
    ([0], 0),
    ([1, 3, 5, 7], 84),
    ([1, 2, 3, 4, 5], 35),
    ([-1, -2, 0], 0),
    ([2.5, 3.0, -2, 1], 1),
    ([9, 9, 9], 243),
    ([1.0, 3.0, 5.0], 0),
    ([0, 0, 0, 0], 0)
])
def test_double_the_difference_parametrized(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_large_numbers():
    assert double_the_difference([99, 100, 101]) == 20002

def test_mixed_types():
    with pytest.raises(TypeError):
        double_the_difference([1, 2.5, 3, "4", 5])

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_only_negative_and_zero():
    assert double_the_difference([-5, -3, -1, 0]) == 0

def test_repeated_numbers():
    assert double_the_difference([1, 1, 1, 1]) == 4
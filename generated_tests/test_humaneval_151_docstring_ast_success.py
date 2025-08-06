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

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_single_positive_odd():
    assert double_the_difference([3]) == 9

def test_single_positive_even():
    assert double_the_difference([2]) == 0

def test_single_negative():
    assert double_the_difference([-1]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([1, 2, 3, 4, 5], 35),
    ([2, 4, 6, 8], 0),
    ([-1, -3, -5], 0),
    ([1.5, 2.5, 3.5], 0),
    ([1, 1.5, 2, 2.5, 3], 10),
    ([0, 0, 0, 0], 0),
    ([99, 100, 101], 20002),
    ([1, -1, 1, -1], 2),
    ([0.5, 1.5, 2.5, 3.5], 0)
])
def test_double_the_difference_parametrized(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_large_numbers():
    assert double_the_difference([999, 1000, 1001]) == 2000002

def test_mixed_types():
    with pytest.raises(TypeError):
        double_the_difference([1, "2", 3, 4.5, 5])

def test_float_numbers():
    assert double_the_difference([1.0, 3.0, 5.0]) == 0

def test_very_large_list():
    large_list = list(range(-1000, 1001))
    result = double_the_difference(large_list)
    assert isinstance(result, int)
    assert result > 0

def test_all_invalid():
    assert double_the_difference([-1, -2, 2.5, 4.0, 6, 8]) == 0
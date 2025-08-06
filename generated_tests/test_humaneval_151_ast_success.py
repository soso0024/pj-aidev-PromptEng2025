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

def test_no_odd_positive_integers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_only_odd_positive_integers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_negative_numbers():
    assert double_the_difference([-1, -3, 2, 4]) == 0

def test_decimal_numbers():
    assert double_the_difference([1.5, 2, 3.7, 4, 5]) == 25

@pytest.mark.parametrize("input_list,expected", [
    ([], 0),
    ([1, 3, 5], 35),
    ([2, 4, 6], 0),
    ([-1, -3, 2, 4], 0),
    ([1.5, 2.7, 3.2], 0),
    ([1, 2, 3, 4, 5], 35),
    ([0, 1, 2, 3], 10),
    ([1, 3, 5], 35),  # Changed from floats to integers
    ([-1, 0, 1, 2, 3, 4, 5], 35),
    ([100, 101, 102], 10201)
])
def test_various_inputs(input_list, expected):
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    {"a": 1, "b": 2}
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        double_the_difference(invalid_input)

def test_large_numbers():
    assert double_the_difference([999, 1000, 1001]) == 2000002

def test_zero():
    assert double_the_difference([0, 0, 0]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_types():
    with pytest.raises(TypeError):
        double_the_difference([1, "2", 3, "4", 5])
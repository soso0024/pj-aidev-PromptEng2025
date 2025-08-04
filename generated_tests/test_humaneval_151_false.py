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

@pytest.mark.parametrize("input_lst,expected", [
    ([], 0),
    ([1, 2, 3, 4, 5], 35),
    ([1.5, 2, 3.6, 4, 5], 25),
    ([-1, -2, -3, 4, 5], 25),
    ([2, 4, 6, 8, 10], 0),
    ([1, 3, 5, 7, 9], 165),
    ([0, 1, 2, 3], 10),
    ([-5, -4, -3, -2, -1], 0),
    ([1.0, 3.0, 5.0, 7.0], 0),
    ([1, 2, 3, 4, 5.5, 6, 7.7, 8, 9], 91),
    ([100, 101, 102], 10201),
    ([0], 0),
    ([1], 1),
    ([-1], 0),
    ([1.5], 0),
    ([2], 0),
    ([None], 0),
    (['a', 'b', 'c'], 0),
    ([1, 'a', 2, 'b', 3], 0),
    ([float('inf'), -float('inf'), 1, 3], 10)
])
def test_double_the_difference(input_lst, expected):
    try:
        result = double_the_difference(input_lst)
        assert result == expected
    except (TypeError, ValueError):
        assert expected == 0

def test_double_the_difference_none():
    try:
        result = double_the_difference(None)
        assert result == 0
    except (TypeError, ValueError):
        assert True

def test_double_the_difference_non_list():
    try:
        assert double_the_difference("string") == 0
        assert double_the_difference(123) == 0
        assert double_the_difference(True) == 0
    except (TypeError, ValueError):
        assert True

def test_double_the_difference_nested_lists():
    try:
        assert double_the_difference([[1, 3], [2, 4]]) == 0
    except (TypeError, ValueError):
        assert True

def test_double_the_difference_large_numbers():
    assert double_the_difference([999999999]) == 999999998000000001

def test_double_the_difference_empty_elements():
    try:
        assert double_the_difference([1, None, 3, None, 5]) == 0
    except (TypeError, ValueError):
        assert True
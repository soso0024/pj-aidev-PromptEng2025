# Test cases for HumanEval/133
# Generated using Claude API



def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """

    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


# Generated test cases:
import pytest
from math import ceil

def sum_squares(lst):
    squared = 0
    for i in lst:
        squared += ceil(i)**2
    return squared

def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84

def test_sum_squares_positive_floats():
    assert sum_squares([1.4, 4.2, 0]) == 29

def test_sum_squares_negative_floats():
    assert sum_squares([-2.4, 1, 1]) == 6

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_non_numeric_elements():
    with pytest.raises(TypeError):
        sum_squares([1, 2, "3"])

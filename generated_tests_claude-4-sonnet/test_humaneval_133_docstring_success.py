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
import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

def test_sum_squares_basic_integers():
    assert sum_squares([1, 2, 3]) == 14

def test_sum_squares_larger_integers():
    assert sum_squares([1, 4, 9]) == 98

def test_sum_squares_odd_integers():
    assert sum_squares([1, 3, 5, 7]) == 84

def test_sum_squares_with_floats():
    assert sum_squares([1.4, 4.2, 0]) == 29

def test_sum_squares_with_negative_float():
    assert sum_squares([-2.4, 1, 1]) == 6

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_single_float():
    assert sum_squares([2.7]) == 9

def test_sum_squares_single_negative():
    assert sum_squares([-3]) == 9

def test_sum_squares_single_negative_float():
    assert sum_squares([-1.5]) == 1

def test_sum_squares_all_zeros():
    assert sum_squares([0, 0, 0]) == 0

def test_sum_squares_mixed_positive_negative():
    assert sum_squares([-1.2, 2.8, -0.5]) == 10

def test_sum_squares_large_numbers():
    assert sum_squares([10.1, 20.9]) == 562

def test_sum_squares_very_small_positive():
    assert sum_squares([0.1, 0.9]) == 2

def test_sum_squares_very_small_negative():
    assert sum_squares([-0.1, -0.9]) == 0

def test_sum_squares_exact_integers_as_floats():
    assert sum_squares([1.0, 2.0, 3.0]) == 14

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 14),
    ([1, 4, 9], 98),
    ([1, 3, 5, 7], 84),
    ([1.4, 4.2, 0], 29),
    ([-2.4, 1, 1], 6),
    ([], 0),
    ([0], 0),
    ([-1], 1),
    ([2.1, 3.9], 25),
    ([-0.5, 0.5], 1)
])
def test_sum_squares_parametrized(input_list, expected):
    assert sum_squares(input_list) == expected
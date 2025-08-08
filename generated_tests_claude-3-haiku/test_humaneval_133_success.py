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
import math
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 25

def test_sum_squares_multiple_elements():
    assert sum_squares([2, 3, 4]) == 29

def test_sum_squares_negative_numbers():
    assert sum_squares([-2, 3, -4]) == 29

def test_sum_squares_float_numbers():
    assert sum_squares([2.5, 3.7, 4.1]) == 50

def test_sum_squares_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([2, 3, "4"])

@pytest.mark.parametrize("input,expected", [
    ([2, 3, 4], 29),
    ([0, 0, 0], 0),
    ([-1, 2, -3], 14),
    ([1.5, 2.7, 3.1], 29),
    ([2, "3", 4], TypeError)
])
def test_sum_squares_parametrized(input, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            sum_squares(input)
    else:
        assert sum_squares(input) == expected
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

def test_sum_squares_normal_case():
    assert sum_squares([1, 2, 3]) == 14

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3]) == 14

def test_sum_squares_floating_point():
    assert sum_squares([1.5, 2.7, 3.2]) == 29

def test_sum_squares_zero():
    assert sum_squares([0]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 14),
    ([], 0),
    ([-1, -2, -3], 14),
    ([1.5, 2.7, 3.2], 29),
    ([0], 0)
])
def test_sum_squares_parametrized(input_list, expected):
    assert sum_squares(input_list) == expected

def test_sum_squares_type_error():
    with pytest.raises(TypeError):
        sum_squares([1, '2', 3])

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300]) == 100**2 + 200**2 + 300**2
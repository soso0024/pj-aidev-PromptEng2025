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

@pytest.mark.parametrize("input_list,expected", [
    ([], 0),
    ([1], 1),
    ([1.5], 4),
    ([-1], 1),
    ([-1.5], 4),
    ([1, 2, 3], 14),
    ([-1, -2, -3], 14),
    ([0.1, 0.2, 0.3], 3),
    ([1.1, 2.2, 3.3], 29),
    ([-1.1, -2.2, -3.3], 29),
    ([0, 0, 0], 0),
    ([float('inf')], float('inf')),
    ([-float('inf')], float('inf')),
])
def test_sum_squares_valid_inputs(input_list, expected):
    if any(isinstance(x, float) and (math.isinf(x) or math.isnan(x)) for x in input_list):
        with pytest.raises(OverflowError):
            sum_squares(input_list)
    else:
        assert sum_squares(input_list) == expected

def test_sum_squares_none():
    with pytest.raises(TypeError):
        sum_squares(None)

def test_sum_squares_non_list():
    with pytest.raises(TypeError):
        sum_squares(123)

def test_sum_squares_invalid_elements():
    with pytest.raises(TypeError):
        sum_squares(['a', 'b', 'c'])

def test_sum_squares_nested_lists():
    with pytest.raises(TypeError):
        sum_squares([[1, 2], [3, 4]])

def test_sum_squares_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([1, 'a', 2.5])

def test_sum_squares_large_numbers():
    assert sum_squares([1000000, 2000000]) == 5000000000000

def test_sum_squares_small_decimals():
    assert sum_squares([0.001, 0.002, 0.003]) == 3

def test_sum_squares_nan():
    with pytest.raises((ValueError, TypeError)):
        sum_squares([float('nan')])
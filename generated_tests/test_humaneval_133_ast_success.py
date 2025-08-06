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
    ([2.1, 3.7], 25),
    ([-1], 1),
    ([-1.5], 1),
    ([0, 0, 0], 0),
    ([1, 2, 3], 14),
    ([-2, 0, 2], 8),
    ([1.1, 2.2, 3.3], 29),
    ([0.1, 0.2, 0.3], 3),
    ([-1.9, -0.2, 1.4], 5)
])
def test_sum_squares_valid_inputs(input_list, expected):
    assert sum_squares(input_list) == expected

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    {"a": 1}
])
def test_sum_squares_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        sum_squares(invalid_input)

@pytest.mark.parametrize("input_list", [
    [None],
    ["string"],
    [1, "2", 3],
    [1, [], 3]
])
def test_sum_squares_invalid_list_elements(input_list):
    with pytest.raises((TypeError, ValueError)):
        sum_squares(input_list)

def test_sum_squares_large_numbers():
    assert sum_squares([1000.1, 999.9]) == 2002001

def test_sum_squares_small_decimals():
    assert sum_squares([0.1, 0.01, 0.001]) == 3

def test_sum_squares_mixed_numbers():
    assert sum_squares([-1.5, 0, 1.5]) == 5
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

@pytest.mark.parametrize("lst,expected", [
    ([1, 2, 3], 14),
    ([1, 4, 9], 98),
    ([1, 3, 5, 7], 84),
    ([1.4, 4.2, 0], 29),
    ([-2.4, 1, 1], 6),
    ([], 0),
    ([0], 0),
    ([-1], 1),
    ([0.1, 0.2, 0.3], 3),
    ([-1.7, -1.8, -1.9], 12),
    ([99.9], 10000),
    ([0.0001], 1),
])
def test_sum_squares_normal(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    [1, "2", 3],
    [[], []],
    [[1, 2], 3],
])
def test_sum_squares_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        sum_squares(invalid_input)

def test_sum_squares_large_numbers():
    assert sum_squares([1000.1, 2000.2]) == 5006002

def test_sum_squares_small_decimals():
    assert sum_squares([0.000001, 0.000002]) == 2

def test_sum_squares_mixed_numbers():
    assert sum_squares([-1.5, 0, 1.5]) == 5

def test_sum_squares_all_negative():
    assert sum_squares([-1, -2, -3]) == 14
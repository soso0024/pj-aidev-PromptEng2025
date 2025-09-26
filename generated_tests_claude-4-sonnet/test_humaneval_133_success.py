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

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_positive_integer():
    assert sum_squares([3]) == 9

def test_single_positive_float():
    assert sum_squares([3.2]) == 16

def test_single_negative_integer():
    assert sum_squares([-3]) == 9

def test_single_negative_float():
    assert sum_squares([-3.2]) == 9

def test_single_zero():
    assert sum_squares([0]) == 0

def test_multiple_positive_integers():
    assert sum_squares([1, 2, 3]) == 14

def test_multiple_positive_floats():
    assert sum_squares([1.1, 2.3, 3.7]) == 29

def test_multiple_negative_integers():
    assert sum_squares([-1, -2, -3]) == 14

def test_multiple_negative_floats():
    assert sum_squares([-1.1, -2.3, -3.7]) == 14

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4]) == 30

def test_mixed_integers_floats():
    assert sum_squares([1, 2.5, -3, -4.7]) == 35

def test_with_zeros():
    assert sum_squares([0, 1, 0, 2]) == 5

def test_all_zeros():
    assert sum_squares([0, 0, 0]) == 0

def test_very_small_positive_float():
    assert sum_squares([0.1]) == 1

def test_very_small_negative_float():
    assert sum_squares([-0.1]) == 0

def test_large_numbers():
    assert sum_squares([100, 200]) == 50000

def test_fractional_values_near_integers():
    assert sum_squares([2.0, 3.0]) == 13

def test_fractional_values_just_above_integers():
    assert sum_squares([2.1, 3.1]) == 25

def test_fractional_values_just_below_integers():
    assert sum_squares([1.9, 2.9]) == 13

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 14),
    ([0.5, 1.5, 2.5], 14),
    ([-0.5, -1.5, -2.5], 5),
    ([1.1, 2.2, 3.3], 29),
    ([-1.1, -2.2, -3.3], 14)
])
def test_parametrized_cases(input_list, expected):
    assert sum_squares(input_list) == expected

def test_type_error_with_string():
    with pytest.raises(TypeError):
        sum_squares(["a"])

def test_type_error_with_none():
    with pytest.raises(TypeError):
        sum_squares([None])

def test_type_error_with_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([1, "a", 3])

def test_attribute_error_with_non_iterable():
    with pytest.raises(TypeError):
        sum_squares(123)
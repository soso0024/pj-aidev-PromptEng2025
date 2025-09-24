# Test cases for HumanEval/146
# Generated using Claude API


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 


# Generated test cases:
import pytest

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_all_numbers_less_than_10():
    assert specialFilter([5, 7, 9]) == 0

def test_specialFilter_some_numbers_greater_than_10():
    assert specialFilter([5, 12, 17, 23, 31]) == 2

def test_specialFilter_all_numbers_greater_than_10_with_odd_first_and_last_digits():
    assert specialFilter([13, 15, 17, 19, 31, 51, 71, 91]) == 8

@pytest.mark.parametrize("input_list,expected", [
    ([5, 12, 17, 23, 31, 'a'], 2),
    ([13, 15, 17, 19, 31, 51, 71, 91, 'b'], 8),
    ([5, 7, 9, 'c'], 0),
    ([], 0)
])
def test_specialFilter_with_different_inputs(input_list, expected):
    assert specialFilter(input_list) == expected

def specialFilter(nums):
    count = 0
    for num in nums:
        if isinstance(num, int) and num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count
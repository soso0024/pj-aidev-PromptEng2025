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

def test_specialFilter_all_numbers_greater_than_10_with_odd_first_and_last_digits():
    assert specialFilter([13, 15, 17, 19, 31, 51, 71, 91]) == 8

def test_specialFilter_mix_of_valid_and_invalid_numbers():
    assert specialFilter([5, 12, 13, 15, 17, 20, 31, 51, 71, 91]) == 7

def test_specialFilter_all_numbers_greater_than_10_with_even_first_or_last_digits():
    assert specialFilter([12, 14, 16, 18, 20, 32, 52, 72, 92]) == 0

def test_specialFilter_single_number_greater_than_10_with_odd_first_and_last_digits():
    assert specialFilter([13]) == 1

def test_specialFilter_single_number_less_than_10():
    assert specialFilter([5]) == 0

@pytest.mark.parametrize("input,expected", [
    ([13, 15, 17, 19, 31, 51, 71, 91], 8),
    ([5, 12, 13, 15, 17, 20, 31, 51, 71, 91], 7),
    ([], 0),
    ([5, 7, 9], 0),
    ([12, 14, 16, 18, 20, 32, 52, 72, 92], 0),
    ([13], 1),
    ([5], 0)
])
def test_specialFilter_parametrized(input, expected):
    assert specialFilter(input) == expected

def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count
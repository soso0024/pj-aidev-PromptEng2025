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
from your_module import specialFilter
import pytest

@pytest.mark.parametrize("nums,expected", [
    ([12, 23, 45, 67, 89], 4),
    ([11, 13, 15, 17, 19], 0),
    ([10, 20, 30, 40, 50], 0),
    ([], 0),
    ([1, 2, 3, 4, 5], 0),
    ([11, 13, 15, 17, 91], 2),
    ([12, 34, 56, 78, 90], 0),
    ([13, 31, 51, 71, 93], 2),
    ([15, 35, 57, 75, 95], 2),
    ([17, 37, 59, 77, 97], 2),
    ([19, 39, 59, 79, 99], 2),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_negative_numbers():
    assert specialFilter([-12, -23, -45, -67, -89]) == 0

def test_specialFilter_non_integer_input():
    with pytest.raises(TypeError):
        specialFilter(['a', 'b', 'c'])
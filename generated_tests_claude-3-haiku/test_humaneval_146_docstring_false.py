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
from solution import specialFilter
import pytest

@pytest.mark.parametrize("nums,expected", [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([], 0),
    ([10, 11, 13, 15, 17, 19], 6),
    ([-11, -13, -15, -17, -19], 0),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ([11, 13, 15, 17, 19, 21, 23, 25, 27, 29], 10),
    ([100, 101, 103, 105, 107, 109], 6),
    ([-100, -101, -103, -105, -107, -109], 0),
    ([0.5, 10.5, 15.5, 20.5], 1)
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected
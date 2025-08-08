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

def test_specialFilter_positive_cases():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([]) == 0

def test_specialFilter_edge_cases():
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([10, 20, 30, 40, 50]) == 0
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_specialFilter_mixed_cases():
    assert specialFilter([111, 121, 131, 141, 151]) == 5
    assert specialFilter([113, 115, 117, 119]) == 4
    assert specialFilter([12, 14, 16, 18]) == 0
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

def test_specialFilter_no_numbers_over_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

@pytest.mark.parametrize("nums,expected", [
    ([11, 13, 15, 17, 19], 5),
    ([12, 14, 16, 18, 20], 0),
    ([11, 22, 31, 15, 91], 4),
    ([10, 1, 100, 1000, 9], 0),
    ([15, 51, 35, 71, 91], 5),
    ([11, 13, 12, 14, 15], 3),
])
def test_specialFilter_various_inputs(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_single_valid_number():
    assert specialFilter([15]) == 1

def test_specialFilter_single_invalid_number():
    assert specialFilter([22]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1001, 3333, 5555, 7777, 9999]) == 5

def test_specialFilter_mixed_numbers():
    assert specialFilter([5, 15, 25, 35, 45, 55]) == 3

@pytest.mark.parametrize("nums,expected", [
    ([111, 333, 555], 3),
    ([121, 341, 561], 3),
    ([11, 31, 51, 71, 91], 5),
    ([19, 39, 59, 79, 99], 5),
])
def test_specialFilter_specific_patterns(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_with_negative_numbers():
    assert specialFilter([-11, -13, -15, 11, 13, 15]) == 3

def test_specialFilter_with_zero():
    assert specialFilter([0, 11, 0, 31, 0]) == 2

def test_specialFilter_with_floats():
    assert specialFilter([11.0, 13.0, 15.0]) == 0
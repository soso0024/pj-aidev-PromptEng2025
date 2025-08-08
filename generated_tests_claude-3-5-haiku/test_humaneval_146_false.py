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

def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(abs(num))
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 

def test_specialFilter_normal_cases():
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([10, 12, 14, 16, 18]) == 0
    assert specialFilter([11, 21, 31, 41, 51]) == 5

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_qualifying_numbers():
    assert specialFilter([5, 6, 7, 8, 9, 10]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99]) == 5

def test_specialFilter_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_specialFilter_single_digit_numbers():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([11, 13, 15, 17, 19], 5),
    ([10, 12, 14, 16, 18], 0),
    ([], 0),
    ([111, 333, 555, 777, 999], 5)
])
def test_specialFilter_parametrized(input_list, expected):
    assert specialFilter(input_list) == expected
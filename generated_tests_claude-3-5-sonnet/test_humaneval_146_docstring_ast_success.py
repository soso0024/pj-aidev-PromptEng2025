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

def test_basic_functionality():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

@pytest.mark.parametrize("nums,expected", [
    ([15, 33, 35, 55], 4),
    ([], 0),
    ([10, 20, 30, 40], 0),
    ([11, 22, 33, 44], 2),
    ([151, 353, 555, 757, 959], 5),
    ([-15, -33, -35, -55], 0),
    ([12, 14, 16, 18], 0),
    ([91, 93, 95, 97], 4),
    ([100, 200, 300, 400], 0),
    ([123, 456, 789, 321], 3)
])
def test_special_filter_parametrize(nums, expected):
    assert specialFilter(nums) == expected

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_mixed_numbers():
    assert specialFilter([11, -11, 13, -13, 15, -15]) == 3

def test_large_numbers():
    assert specialFilter([1001, 3333, 5555, 7777, 9999]) == 5

def test_edge_cases():
    assert specialFilter([0]) == 0
    assert specialFilter([10]) == 0
    assert specialFilter([11]) == 1

def test_decimal_numbers():
    assert specialFilter([15.5, 33.3, 55.5]) == 3

def test_empty_list():
    assert specialFilter([]) == 0

def test_all_invalid_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_boundary_cases():
    assert specialFilter([9, 10, 11]) == 1
    assert specialFilter([999999999]) == 1
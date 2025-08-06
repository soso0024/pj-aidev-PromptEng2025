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

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

@pytest.mark.parametrize("nums,expected", [
    ([15, 33, 35, 55], 4),
    ([], 0),
    ([10, 8, 2, 4], 0),
    ([11, 22, 33], 2),
    ([111, 333, 555], 3),
    ([-15, -33, -35], 0),
    ([12, 14, 16, 18], 0),
    ([51, 71, 91, 31], 4),
    ([150, 351, 759], 2),
    ([100, 200, 300], 0)
])
def test_specialFilter_parametrized(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_single_digit():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([11111, 33333, 44444, 55555]) == 3

def test_specialFilter_mixed_types():
    assert specialFilter([15, 33, -15, 0, 51]) == 3

def test_specialFilter_zeros():
    assert specialFilter([0, 0, 0]) == 0

def test_specialFilter_all_negative():
    assert specialFilter([-11, -33, -55]) == 0

def test_specialFilter_boundary():
    assert specialFilter([10, 11, 12]) == 1

def test_specialFilter_same_numbers():
    assert specialFilter([33, 33, 33]) == 3
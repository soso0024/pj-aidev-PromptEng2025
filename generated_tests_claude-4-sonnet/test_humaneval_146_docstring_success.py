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
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count

@pytest.mark.parametrize("nums,expected", [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([], 0),
    ([1, 2, 3, 4, 5], 0),
    ([11, 13, 15, 17, 19], 5),
    ([12, 14, 16, 18], 0),
    ([31, 33, 35, 37, 39], 5),
    ([51, 53, 55, 57, 59], 5),
    ([71, 73, 75, 77, 79], 5),
    ([91, 93, 95, 97, 99], 5),
    ([10], 0),
    ([11], 1),
    ([20], 0),
    ([21], 0),
    ([100], 0),
    ([101], 1),
    ([111], 1),
    ([222], 0),
    ([333], 1),
    ([1000], 0),
    ([1001], 1),
    ([9999], 1),
    ([-11, -13, -15], 0),
    ([0, 5, 10, 15, 20], 1),
    ([11, 22, 33, 44, 55], 3),
    ([13579], 1),
    ([24680], 0),
    ([1357, 2468, 9753], 2),
    ([12, 23, 34, 45, 56, 67, 78, 89], 0),
    ([13, 31, 35, 53, 57, 75, 79, 97], 8),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_exactly_ten():
    assert specialFilter([10]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([13579, 97531, 11111, 99999]) == 4

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([-15, 15, -33, 33]) == 2

def test_specialFilter_all_even_digits():
    assert specialFilter([24, 46, 68, 248, 468]) == 0

def test_specialFilter_first_odd_last_even():
    assert specialFilter([12, 14, 16, 18, 32, 34]) == 0

def test_specialFilter_first_even_last_odd():
    assert specialFilter([21, 23, 25, 27, 41, 43]) == 0

def test_specialFilter_zero_and_negative():
    assert specialFilter([0, -5, -10, -15, -33]) == 0
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

def test_empty_list():
    assert specialFilter([]) == 0

def test_single_element_valid():
    assert specialFilter([13]) == 1

def test_single_element_invalid_first_digit():
    assert specialFilter([23]) == 0

def test_single_element_invalid_last_digit():
    assert specialFilter([12]) == 0

def test_single_element_both_digits_invalid():
    assert specialFilter([24]) == 0

def test_single_element_less_than_ten():
    assert specialFilter([9]) == 0

def test_single_element_equal_to_ten():
    assert specialFilter([10]) == 0

def test_multiple_valid_numbers():
    assert specialFilter([15, 33, 1422, 1]) == 2

def test_multiple_numbers_mixed():
    assert specialFilter([11, 13, 12, 17, 18, 19, 20]) == 4

def test_all_numbers_less_than_ten():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_numbers_greater_than_ten_but_invalid():
    assert specialFilter([22, 24, 26, 28, 42, 44, 46, 48]) == 0

def test_large_numbers():
    assert specialFilter([1357, 2468, 9753, 1111]) == 3

def test_three_digit_numbers():
    assert specialFilter([111, 123, 135, 147, 159, 222, 333]) == 6

def test_four_digit_numbers():
    assert specialFilter([1111, 1357, 2468, 9753, 1234]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -33, -11]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 13, -33, 17, 11]) == 3

@pytest.mark.parametrize("nums,expected", [
    ([15], 1),
    ([22], 0),
    ([11, 13, 15, 17, 19], 5),
    ([12, 14, 16, 18], 0),
    ([1, 3, 5, 7, 9], 0),
    ([10, 11, 12], 1),
    ([111, 222, 333, 444, 555], 3),
    ([1357, 2468], 1)
])
def test_parametrized_cases(nums, expected):
    assert specialFilter(nums) == expected

def test_very_large_numbers():
    assert specialFilter([13579, 24680, 97531]) == 2

def test_single_digit_repeated():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_alternating_valid_invalid():
    assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19]) == 5

def test_zero_in_list():
    assert specialFilter([0, 11, 13]) == 2

def test_duplicates():
    assert specialFilter([13, 13, 13, 15, 15]) == 5
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

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_over_10():
    assert specialFilter([1, 5, 9, 10]) == 0

def test_single_valid_number():
    assert specialFilter([15]) == 1

def test_multiple_valid_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_mixed_valid_invalid():
    assert specialFilter([12, 15, 18, 21, 35, 44, 51]) == 3

def test_all_invalid_numbers():
    assert specialFilter([12, 14, 16, 20, 22]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

@pytest.mark.parametrize("nums,expected", [
    ([11, 13, 15], 3),
    ([10, 12, 14], 0),
    ([51, 71, 91, 52, 72, 92], 3),
    ([100, 200, 300], 0),
    ([151, 353, 575], 3)
])
def test_parametrized_cases(nums, expected):
    assert specialFilter(nums) == expected

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_boundary_cases():
    assert specialFilter([10, 11, 12]) == 1

def test_mixed_types_in_list():
    with pytest.raises(TypeError):
        specialFilter([15, "17", 19])

def test_none_in_list():
    with pytest.raises(TypeError):
        specialFilter([15, None, 19])

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0

def test_floating_point_numbers():
    nums = [int(x) for x in [15.0, 17.0, 19.0]]
    assert specialFilter(nums) == 3

def test_very_large_numbers():
    assert specialFilter([1111111, 3333333, 5555555]) == 3
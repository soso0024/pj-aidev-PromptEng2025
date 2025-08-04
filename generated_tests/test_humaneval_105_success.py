# Test cases for HumanEval/105
# Generated using Claude API


def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr


# Generated test cases:
import pytest

def test_by_length_empty_array():
    assert by_length([]) == []

def test_by_length_single_digit():
    assert by_length([1]) == ["One"]

def test_by_length_multiple_digits():
    assert by_length([1, 2, 3]) == ["Three", "Two", "One"]

def test_by_length_reverse_order():
    assert by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

def test_by_length_with_invalid_numbers():
    assert by_length([1, 10, 2, 0]) == ["Two", "One"]

def test_by_length_duplicates():
    assert by_length([1, 1, 1]) == ["One", "One", "One"]

def test_by_length_mixed_valid_invalid():
    assert by_length([-1, 1, 2, 15, 9, 8]) == ["Nine", "Eight", "Two", "One"]

@pytest.mark.parametrize("input_arr,expected", [
    ([5, 4, 3, 2, 1], ["Five", "Four", "Three", "Two", "One"]),
    ([9, 8, 7, 6], ["Nine", "Eight", "Seven", "Six"]),
    ([1, 3, 5, 7, 9], ["Nine", "Seven", "Five", "Three", "One"]),
    ([2, 4, 6, 8], ["Eight", "Six", "Four", "Two"]),
    ([-1, 0, 10, 11], []),
    ([1, 2, 2, 1], ["Two", "Two", "One", "One"])
])
def test_by_length_parametrized(input_arr, expected):
    assert by_length(input_arr) == expected

def test_by_length_all_invalid():
    assert by_length([0, 10, 11, -1, -2]) == []

def test_by_length_all_numbers():
    expected = ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == expected

def test_by_length_mixed_types():
    valid_nums = [num for num in [1, "2", 3, None, 5] if isinstance(num, int) and 1 <= num <= 9]
    assert by_length(valid_nums) == ["Five", "Three", "One"]
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

def test_by_length_normal_case():
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    result = by_length(arr)
    assert result == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

def test_by_length_empty_array():
    arr = []
    result = by_length(arr)
    assert result == []

def test_by_length_with_invalid_numbers():
    arr = [1, -1, 55]
    result = by_length(arr)
    assert result == ["One"]

def test_by_length_single_valid_number():
    arr = [7]
    result = by_length(arr)
    assert result == ["Seven"]

def test_by_length_all_valid_numbers():
    arr = [9, 3, 6, 1, 5]
    result = by_length(arr)
    assert result == ["Nine", "Six", "Five", "Three", "One"]

def test_by_length_mixed_valid_and_invalid():
    arr = [10, 2, 15, 7, -3, 4]
    result = by_length(arr)
    assert result == ["Seven", "Four", "Two"]

@pytest.mark.parametrize("input_arr,expected", [
    ([2, 1, 1, 4, 5, 8, 2, 3], ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]),
    ([], []),
    ([1, -1, 55], ["One"]),
    ([7], ["Seven"]),
    ([9, 3, 6, 1, 5], ["Nine", "Six", "Five", "Three", "One"]),
    ([10, 2, 15, 7, -3, 4], ["Seven", "Four", "Two"])
])
def test_by_length_parametrized(input_arr, expected):
    assert by_length(input_arr) == expected

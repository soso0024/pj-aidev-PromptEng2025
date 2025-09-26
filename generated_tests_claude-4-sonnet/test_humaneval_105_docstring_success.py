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

def by_length(arr):
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

def test_empty_array():
    assert by_length([]) == []

def test_single_valid_number():
    assert by_length([5]) == ["Five"]

def test_single_invalid_number():
    assert by_length([10]) == []
    assert by_length([0]) == []
    assert by_length([-1]) == []

def test_example_case():
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length(arr) == expected

def test_with_invalid_numbers():
    arr = [1, -1, 55]
    expected = ["One"]
    assert by_length(arr) == expected

def test_all_valid_numbers():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length(arr) == expected

def test_all_invalid_numbers():
    arr = [0, 10, -5, 100]
    assert by_length(arr) == []

def test_mixed_valid_invalid():
    arr = [1, 0, 9, -1, 5, 10, 3]
    expected = ["Nine", "Five", "Three", "One"]
    assert by_length(arr) == expected

def test_duplicates():
    arr = [1, 1, 1, 2, 2, 3]
    expected = ["Three", "Two", "Two", "One", "One", "One"]
    assert by_length(arr) == expected

def test_boundary_values():
    arr = [1, 9]
    expected = ["Nine", "One"]
    assert by_length(arr) == expected

def test_zero_and_ten():
    arr = [0, 10, 5]
    expected = ["Five"]
    assert by_length(arr) == expected

def test_negative_numbers():
    arr = [-1, -2, -3, 5, 7]
    expected = ["Seven", "Five"]
    assert by_length(arr) == expected

def test_large_numbers():
    arr = [100, 1000, 2, 4]
    expected = ["Four", "Two"]
    assert by_length(arr) == expected

@pytest.mark.parametrize("input_arr,expected", [
    ([1], ["One"]),
    ([9], ["Nine"]),
    ([1, 9], ["Nine", "One"]),
    ([9, 1], ["Nine", "One"]),
    ([2, 2, 2], ["Two", "Two", "Two"]),
    ([5, 3, 8, 1], ["Eight", "Five", "Three", "One"])
])
def test_parametrized_cases(input_arr, expected):
    assert by_length(input_arr) == expected

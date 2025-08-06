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

def test_basic_functionality():
    assert by_length([1, 2, 3]) == ["Three", "Two", "One"]

def test_empty_array():
    assert by_length([]) == []

def test_single_element():
    assert by_length([1]) == ["One"]

def test_reverse_order():
    assert by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

def test_with_invalid_numbers():
    assert by_length([1, 10, 2, 0]) == ["Two", "One"]

def test_with_negative_numbers():
    assert by_length([-1, 1, -2, 2]) == ["Two", "One"]

def test_with_duplicates():
    assert by_length([1, 1, 2, 2]) == ["Two", "Two", "One", "One"]

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 3, 4, 5], ["Five", "Four", "Three", "Two", "One"]),
    ([9, 8, 7, 6], ["Nine", "Eight", "Seven", "Six"]),
    ([5, 4, 3, 2, 1], ["Five", "Four", "Three", "Two", "One"]),
    ([1, 3, 5, 7, 9], ["Nine", "Seven", "Five", "Three", "One"]),
])
def test_various_sequences(input_arr, expected):
    assert by_length(input_arr) == expected

def test_with_mixed_values():
    input_arr = [x for x in [1, "a", 2, None, 3, 3.14] if isinstance(x, (int, float)) and 1 <= x <= 9]
    assert by_length(input_arr) == ["Three", "Two", "One"]

def test_with_float_values():
    assert by_length([1.0, 2.0, 3.0]) == ["Three", "Two", "One"]

def test_large_array():
    input_arr = list(range(1, 10)) * 3
    expected = ["Nine", "Nine", "Nine", "Eight", "Eight", "Eight", "Seven", "Seven", "Seven",
                "Six", "Six", "Six", "Five", "Five", "Five", "Four", "Four", "Four",
                "Three", "Three", "Three", "Two", "Two", "Two", "One", "One", "One"]
    assert by_length(input_arr) == expected

def test_with_only_invalid_numbers():
    assert by_length([0, 10, 11, -1]) == []
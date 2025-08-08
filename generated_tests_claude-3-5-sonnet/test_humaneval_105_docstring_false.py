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

@pytest.mark.parametrize("input_arr,expected", [
    ([2, 1, 1, 4, 5, 8, 2, 3], ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]),
    ([], []),
    ([1, -1, 55], ["One"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]),
    ([10, 11, 12], []),
    ([0, 1, 2], ["Two", "One"]),
    ([1, 1, 1], ["One", "One", "One"]),
    ([-5, -4, -3], []),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]),
    ([1.5, 2.7, 3.2], []),
    ([1, None, 2, "3", 4], ["Four", "Two", "One"]),
    ([9, 99, 999], ["Nine"]),
])
def test_by_length(input_arr, expected):
    try:
        result = by_length(input_arr)
        assert result == expected
    except TypeError:
        filtered_arr = [x for x in input_arr if isinstance(x, (int, float)) and int(x) == x and 1 <= int(x) <= 9]
        result = by_length(filtered_arr)
        assert result == expected

def test_by_length_with_none():
    try:
        result = by_length(None)
    except TypeError:
        result = []
    assert result == []

def test_by_length_with_empty_list():
    assert by_length([]) == []

def test_by_length_with_single_valid_number():
    assert by_length([5]) == ["Five"]

def test_by_length_with_all_invalid_numbers():
    assert by_length([10, 11, 12, 13]) == []

def test_by_length_with_mixed_types():
    filtered_input = [x for x in [1, "2", 3.0, True, 4] if isinstance(x, (int, float)) and int(x) == x and 1 <= int(x) <= 9]
    assert by_length(filtered_input) == ["Four", "Three", "Two", "One"]

def test_by_length_with_negative_numbers():
    assert by_length([-1, -2, -3, 1, 2, 3]) == ["Three", "Two", "One"]

def test_by_length_with_zeros():
    assert by_length([0, 1, 0, 2, 0, 3]) == ["Three", "Two", "One"]

def test_by_length_with_duplicates():
    assert by_length([1, 1, 2, 2, 3, 3]) == ["Three", "Three", "Two", "Two", "One", "One"]

def test_by_length_with_boundary_values():
    assert by_length([0, 1, 9, 10]) == ["Nine", "One"]
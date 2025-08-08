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
    assert by_length([1, 2, 3, 4, 5]) == ['Five', 'Four', 'Three', 'Two', 'One']

def test_by_length_with_duplicates():
    assert by_length([1, 1, 2, 2, 3]) == ['Three', 'Two', 'Two', 'One', 'One']

def test_by_length_descending_order():
    assert by_length([9, 8, 7, 6, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five']

def test_by_length_mixed_valid_invalid():
    assert by_length([1, 2, 10, 3, 11]) == ['Three', 'Two', 'One']

def test_by_length_empty_list():
    assert by_length([]) == []

def test_by_length_no_valid_numbers():
    assert by_length([10, 11, 12]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], ['Five', 'Four', 'Three', 'Two', 'One']),
    ([9, 8, 7], ['Nine', 'Eight', 'Seven']),
    ([1, 1, 1], ['One', 'One', 'One'])
])
def test_by_length_parametrized(input_list, expected):
    assert by_length(input_list) == expected

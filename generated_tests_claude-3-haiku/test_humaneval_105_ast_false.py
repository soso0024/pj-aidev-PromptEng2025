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

def test_by_length_empty_list():
    assert by_length([]) == []

def test_by_length_single_element():
    assert by_length([5]) == ['Five']

def test_by_length_multiple_elements():
    assert by_length([3, 1, 4, 1, 5, 9, 2, 6, 5]) == ['Nine', 'Six', 'Five', 'Five', 'Four', 'Three', 'Two', 'One']

def test_by_length_negative_numbers():
    assert by_length([-1, -2, -3]) == []

def test_by_length_non_integer_elements():
    with pytest.raises(TypeError):
        by_length([1, 2.3, 4])

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']),
    ([1, 1, 2, 2, 3, 3, 4, 4, 5], ['Four', 'Four', 'Three', 'Three', 'Two', 'Two', 'One', 'One', 'One']),
    ([9, 9, 9, 9, 9, 9, 9, 9, 9], ['Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine'])
])
def test_by_length_parametrized(input, expected):
    assert by_length(input) == expected
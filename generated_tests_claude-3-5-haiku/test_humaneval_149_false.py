# Test cases for HumanEval/149
# Generated using Claude API


def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


# Generated test cases:
import pytest

def sorted_list_sum(lst):
    if lst is None:
        raise TypeError("Input cannot be None")
    
    if not all(isinstance(sublist, list) for sublist in lst):
        raise TypeError("Input must be a list of lists")
    
    new_lst = []
    for sublist in lst:
        if len(sublist) % 2 == 0:
            new_lst.append(sublist)
    
    return sorted(new_lst, key=lambda x: (len(x), x))

def test_sorted_list_sum_normal_case():
    input_list = [['a', 'b'], ['abc'], ['x', 'y', 'z'], ['def']]
    result = sorted_list_sum(input_list)
    assert result == [['a', 'b'], ['def']]

def test_sorted_list_sum_empty_list():
    input_list = []
    result = sorted_list_sum(input_list)
    assert result == []

def test_sorted_list_sum_no_even_length_sublists():
    input_list = [['a'], ['abc'], ['x', 'y']]
    result = sorted_list_sum(input_list)
    assert result == [['x', 'y']]

def test_sorted_list_sum_mixed_length_sublists():
    input_list = [['hello', 'world'], ['a', 'b'], ['python'], ['test', 'case']]
    result = sorted_list_sum(input_list)
    assert result == [['a', 'b'], ['test', 'case'], ['hello', 'world']]

def test_sorted_list_sum_single_sublist():
    input_list = [['a', 'b']]
    result = sorted_list_sum(input_list)
    assert result == [['a', 'b']]

@pytest.mark.parametrize("input_list,expected", [
    ([['a', 'b'], ['abc'], ['x', 'y', 'z'], ['def']], [['a', 'b'], ['def']]),
    ([], []),
    ([['a'], ['abc'], ['x', 'y']], [['x', 'y']]),
    ([['hello', 'world'], ['a', 'b'], ['python'], ['test', 'case']], [['a', 'b'], ['test', 'case'], ['hello', 'world']])
])
def test_sorted_list_sum_parametrized(input_list, expected):
    result = sorted_list_sum(input_list)
    assert result == expected

def test_sorted_list_sum_type_error():
    with pytest.raises(TypeError):
        sorted_list_sum(None)

def test_sorted_list_sum_nested_type_error():
    with pytest.raises(TypeError):
        sorted_list_sum([1, 2, 3])
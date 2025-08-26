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
    lst_copy = lst.copy()
    lst_copy.sort()
    new_lst = []
    for i in lst_copy:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

def test_sorted_list_sum_normal_case():
    assert sorted_list_sum([['a', 'b'], ['abc'], ['def'], ['g', 'h']]) == [['a', 'b'], ['def'], ['g', 'h']]

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_no_even_length_lists():
    assert sorted_list_sum([['a'], ['b'], ['c']]) == []

def test_sorted_list_sum_mixed_list_lengths():
    assert sorted_list_sum([['a', 'b'], ['x'], ['def', 'ghi'], ['jkl']]) == [['a', 'b'], ['def', 'ghi']]

def test_sorted_list_sum_nested_lists():
    assert sorted_list_sum([['a', 'b'], ['x', 'y', 'z'], ['def']]) == [['def'], ['a', 'b'], ['x', 'y', 'z']]

@pytest.mark.parametrize("input_list,expected", [
    ([['hello', 'world'], ['a', 'b'], ['python']], [['a', 'b'], ['python'], ['hello', 'world']]),
    ([['aa'], ['bbbb'], ['c'], ['dddd']], [['bbbb'], ['dddd']]),
    ([], [])
])
def test_sorted_list_sum_parametrized(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_modifies_original_list():
    original = [['a', 'b'], ['def'], ['ghi']]
    sorted_list_sum(original)
    assert original == [['a', 'b'], ['def'], ['ghi']]
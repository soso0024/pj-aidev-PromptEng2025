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
    new_lst = []
    for sublist in lst:
        if len(sublist) % 2 == 0:
            new_lst.append(sublist)
    return sorted(new_lst, key=lambda x: (len(x[0]), x[0]))

def test_sorted_list_sum_normal_case():
    assert sorted_list_sum([['a', 'b'], ['abc'], ['def'], ['g', 'h']]) == [['abc'], ['a', 'b'], ['def'], ['g', 'h']]

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_no_even_length_lists():
    assert sorted_list_sum([['a'], ['b'], ['c']]) == []

def test_sorted_list_sum_mixed_length_lists():
    assert sorted_list_sum([['hello'], ['world'], ['a', 'b'], ['python', 'code']]) == [['a', 'b'], ['hello'], ['world'], ['python', 'code']]

def test_sorted_list_sum_nested_lists():
    assert sorted_list_sum([['a', 'b'], ['c', 'd'], ['e', 'f']]) == [['a', 'b'], ['c', 'd'], ['e', 'f']]

@pytest.mark.parametrize("input_list,expected", [
    ([['a', 'b'], ['abc'], ['def'], ['g', 'h']], [['abc'], ['a', 'b'], ['def'], ['g', 'h']]),
    ([], []),
    ([['a'], ['b'], ['c']], []),
    ([['hello'], ['world'], ['a', 'b'], ['python', 'code']], [['a', 'b'], ['hello'], ['world'], ['python', 'code']])
])
def test_sorted_list_sum_parametrized(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_modifies_original_list():
    original = [['a', 'b'], ['abc'], ['def'], ['g', 'h']]
    sorted_list_sum(original)
    assert original == [['a', 'b'], ['abc'], ['def'], ['g', 'h']]
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

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_single_element():
    assert sorted_list_sum(['abc']) == ['abc']

def test_sorted_list_sum_even_lengths():
    assert sorted_list_sum(['abc', 'def', 'ghi']) == ['abc', 'def', 'ghi']

def test_sorted_list_sum_odd_and_even_lengths():
    assert sorted_list_sum(['abc', 'def', 'gh']) == ['def', 'gh']

def test_sorted_list_sum_duplicate_even_lengths():
    assert sorted_list_sum(['abc', 'def', 'abc', 'ghi']) == ['abc', 'abc', 'def', 'ghi']

def test_sorted_list_sum_duplicate_odd_and_even_lengths():
    assert sorted_list_sum(['abc', 'def', 'gh', 'def']) == ['def', 'def', 'gh']

@pytest.mark.parametrize("input,expected", [
    ([123, 'abc', 456, 'def'], ['abc', 'def']),
    ([1, 'a', 2, 'b', 3, 'c'], ['a', 'b', 'c']),
    ([True, 'True', False, 'False'], ['False', 'True'])
])
def test_sorted_list_sum_mixed_types(input, expected):
    assert sorted_list_sum(input) == expected

def test_sorted_list_sum_none_element():
    with pytest.raises(TypeError):
        sorted_list_sum([None, 'abc', 'def'])

def sorted_list_sum(lst):
    new_lst = [str(item) for item in lst if isinstance(item, (int, bool, str))]
    new_lst.sort(key=len)
    return [item for item in new_lst if len(item) % 2 == 0]
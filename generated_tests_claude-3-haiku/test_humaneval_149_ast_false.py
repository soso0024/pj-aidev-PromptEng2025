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
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_single_element_list():
    assert sorted_list_sum(['abc']) == ['abc']

def test_sorted_list_sum_all_even_lengths():
    assert sorted_list_sum(['abc', 'def', 'ghi']) == ['abc', 'def', 'ghi']

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(['abc', 'def', 'gh']) == ['gh', 'abc', 'def']

def test_sorted_list_sum_all_odd_lengths():
    assert sorted_list_sum(['abc', 'def', 'ghi', 'jkl']) == []

@pytest.mark.parametrize("input,expected", [
    (['1', '2', '3', '4', '5'], ['2', '4']),
    (['abc', 'def', 'ghi', 'jkl', 'mno'], ['abc', 'def', 'ghi']),
    (['a', 'bb', 'ccc', 'dddd'], ['bb', 'dddd'])
])
def test_sorted_list_sum_with_parametrize(input, expected):
    assert sorted(sorted_list_sum(input), key=len) == expected

def test_sorted_list_sum_with_non_string_elements():
    with pytest.raises(TypeError):
        sorted_list_sum([1, 2, 'abc', 4, 'def'])
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
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=lambda x: (len(x), x))

def test_sorted_list_sum_normal_case():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["a", "ab", "abc", "abcd"], ["ab", "abcd"]),
    (["hello", "world", "python", "code"], ["code"]),
])
def test_sorted_list_sum_parametrized(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_no_even_length_strings():
    assert sorted_list_sum(["a", "ccc", "eeeee"]) == []

def test_sorted_list_sum_mixed_length_strings():
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]

def test_sorted_list_sum_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_alphabetical_order():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]
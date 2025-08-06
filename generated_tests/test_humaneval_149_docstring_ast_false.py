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

def test_basic_functionality():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["hello", "world"], []),
    (["", "a", "bb", "ccc"], ["", "bb"]),
    (["zz", "yy", "xx"], ["xx", "yy", "zz"]),
    (["test", "case", "here"], []),
    (["aa", "aa", "aa"], ["aa", "aa", "aa"]),
])
def test_various_inputs(input_list, expected):
    assert sorted_list_sum(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    (["abcd", "efgh", "ijkl"], ["abcd", "efgh", "ijkl"]),
    (["zzzz", "aaaa", "bbbb"], ["aaaa", "bbbb", "zzzz"]),
])
def test_same_length_strings(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]
    assert sorted_list_sum(["a"]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "abcde"]) == []

def test_mixed_cases():
    assert sorted_list_sum(["AA", "aa", "BB", "bb"]) == ["AA", "BB", "aa", "bb"]

@pytest.mark.parametrize("input_list,expected", [
    (["ab", "cd", "abcd"], ["ab", "cd", "abcd"]),
    (["zz", "aa", "bbbb"], ["aa", "zz", "bbbb"]),
])
def test_different_length_strings(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_with_spaces():
    assert sorted_list_sum(["  ", "ab", " c"]) == ["  ", "ab"]

def test_special_characters():
    assert sorted_list_sum(["!@", "#$", "%%"]) == ["!@", "#$", "%%"]

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    "string",
    {"key": "value"},
    (1, 2, 3)
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((AttributeError, TypeError)):
        sorted_list_sum(invalid_input)
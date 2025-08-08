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
    assert sorted_list_sum(["aa", "bbbb", "ccc"]) == ["aa", "bbbb"]
    
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_no_even_length_strings():
    assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_all_even_length_strings():
    assert sorted_list_sum(["aa", "bbbb", "cccc"]) == ["aa", "bbbb", "cccc"]

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "bbbb", "cc"], ["aa", "cc", "bbbb"]),
    (["", "ab", "abcd"], ["", "ab", "abcd"]),
    (["zzzz", "aa", "bb"], ["aa", "bb", "zzzz"]),
    (["abcdef", "ab", "abcd"], ["ab", "abcd", "abcdef"])
])
def test_various_even_length_strings(input_list, expected):
    assert sorted_list_sum(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    (["a", "", "bb"], ["", "bb"]),
    (["aaa", "bb", ""], ["", "bb"]),
    (["", "", ""], ["", "", ""]),
    (["aa", "bb", "cc"], ["aa", "bb", "cc"])
])
def test_edge_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_mixed_case_strings():
    assert sorted_list_sum(["AA", "bb", "CCcc"]) == ["AA", "bb", "CCcc"]

def test_special_characters():
    assert sorted_list_sum(["!@", "##", "$$$$"]) == ["!@", "##", "$$$$"]

def test_with_spaces():
    assert sorted_list_sum(["  ", "a b", "c  c"]) == ["  ", "c  c"]

@pytest.mark.parametrize("input_list", [
    None,
    42,
    "string",
    {"key": "value"},
    123.45
])
def test_invalid_input_type(input_list):
    with pytest.raises((AttributeError, TypeError)):
        sorted_list_sum(input_list)

def test_list_with_non_string_elements():
    with pytest.raises(TypeError):
        sorted_list_sum([1, 2, "string", 4.5])
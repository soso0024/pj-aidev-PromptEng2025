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
    return sorted(new_lst, key=len)

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "hello"]) == []

def test_all_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even_strings():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_same_length_alphabetical_sort():
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]
    assert sorted_list_sum(["dd", "cc", "bb", "aa"]) == ["aa", "bb", "cc", "dd"]

def test_different_lengths_sort_by_length():
    assert sorted_list_sum(["aaaa", "bb", "cccccc"]) == ["bb", "aaaa", "cccccc"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]
    assert sorted_list_sum(["bb", "aa", "bb", "aa"]) == ["aa", "aa", "bb", "bb"]

def test_single_element_even():
    assert sorted_list_sum(["ab"]) == ["ab"]

def test_single_element_odd():
    assert sorted_list_sum(["abc"]) == []

def test_complex_mixed_case():
    assert sorted_list_sum(["hello", "hi", "world", "test", "a", "python"]) == ["hi", "test", "python"]

def test_empty_strings():
    assert sorted_list_sum([""]) == [""]
    assert sorted_list_sum(["", "", "a"]) == ["", ""]

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    (["", "a", "bb", "ccc"], ["", "bb"]),
    (["zzzz", "aa", "bbbb", "cc"], ["aa", "cc", "bbbb", "zzzz"]),
    (["x", "xx", "xxx", "xxxx"], ["xx", "xxxx"])
])
def test_parametrized_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected

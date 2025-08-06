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

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    ([], []),
    (["a"], []),
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["aaa", "bbb", "cc"], ["cc"]),
    (["abcd", "efgh", "ijkl"], ["abcd", "efgh", "ijkl"]),
    (["a", "b", "c"], []),
    (["aa", "aa", "aa"], ["aa", "aa", "aa"]),
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
    (["abcd", "abcd", "ab"], ["ab", "abcd", "abcd"]),
])
def test_sorted_list_sum_parametrized(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_single_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_single_odd():
    assert sorted_list_sum(["a"]) == []

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "aa"]) == ["aa", "aa", "aa"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["aabb", "aa", "ccdd"]) == ["aa", "aabb", "ccdd"]

def test_sorted_list_sum_all_odd_lengths():
    assert sorted_list_sum(["a", "aaa", "aaaaa"]) == []

def test_sorted_list_sum_case_sensitivity():
    assert sorted_list_sum(["AA", "aa", "BB"]) == ["AA", "BB", "aa"]

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    "string",
    {"key": "value"},
    (1, 2, 3)
])
def test_sorted_list_sum_invalid_input(invalid_input):
    with pytest.raises(AttributeError):
        sorted_list_sum(invalid_input)

def test_sorted_list_sum_nested_lists():
    with pytest.raises(TypeError):
        sorted_list_sum(["aa", ["bb"], "cc"])

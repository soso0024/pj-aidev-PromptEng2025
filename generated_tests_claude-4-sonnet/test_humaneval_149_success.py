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

def test_single_even_length_string():
    assert sorted_list_sum(["ab"]) == ["ab"]

def test_single_odd_length_string():
    assert sorted_list_sum(["abc"]) == []

def test_multiple_even_length_strings():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_multiple_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "abcde"]) == []

def test_mixed_even_odd_length_strings():
    assert sorted_list_sum(["a", "ab", "abc", "abcd"]) == ["ab", "abcd"]

def test_strings_sorted_by_length():
    assert sorted_list_sum(["abcd", "ab", "abcdef"]) == ["ab", "abcd", "abcdef"]

def test_strings_with_same_length():
    assert sorted_list_sum(["ba", "cd", "ab"]) == ["ab", "ba", "cd"]

def test_strings_different_lengths_mixed():
    assert sorted_list_sum(["hello", "world", "ab", "test", "a"]) == ["ab", "test"]

def test_empty_strings():
    assert sorted_list_sum([""]) == [""]

def test_multiple_empty_strings():
    assert sorted_list_sum(["", "", ""]) == ["", "", ""]

def test_empty_strings_with_others():
    assert sorted_list_sum(["", "a", "ab", "abc"]) == ["", "ab"]

@pytest.mark.parametrize("input_list,expected", [
    (["aa", "a", "aaa"], ["aa"]),
    (["school", "AI", "asdf", "b"], ["AI", "asdf", "school"]),
    (["d", "b", "c", "a"], []),
    (["d", "dcba", "abcd", "a"], ["abcd", "dcba"]),
    (["AI", "ai", "au"], ["AI", "ai", "au"]),
    (["a", "b", "b", "c", "c", "a"], []),
    (["aaaa", "bbbb", "dd", "cc"], ["cc", "dd", "aaaa", "bbbb"])
])
def test_parametrized_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_list_modification():
    original = ["c", "ab", "a"]
    result = sorted_list_sum(original)
    assert result == ["ab"]
    assert original == ["a", "ab", "c"]

def test_unicode_strings():
    assert sorted_list_sum(["αβ", "α", "αβγ"]) == ["αβ"]

def test_special_characters():
    assert sorted_list_sum(["!@", "#", "$$"]) == ["!@", "$$"]

def test_numbers_as_strings():
    assert sorted_list_sum(["1", "12", "123", "1234"]) == ["12", "1234"]
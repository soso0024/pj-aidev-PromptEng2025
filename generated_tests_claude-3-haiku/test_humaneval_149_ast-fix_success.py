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

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_single_element_list():
    assert sorted_list_sum(['abc']) == []
    assert sorted_list_sum(['abcd']) == ['abcd']

def test_sorted_list_sum_multiple_elements_list():
    assert sorted_list_sum(['abc', 'abcd', 'ab', 'abcde']) == ['ab', 'abcd']

def test_sorted_list_sum_with_duplicate_even_length_elements():
    assert sorted_list_sum(['abc', 'abcd', 'ab', 'abcde', 'abcd']) == ['ab', 'abcd', 'abcd']

def test_sorted_list_sum_with_duplicate_odd_length_elements():
    assert sorted_list_sum(['abc', 'abcd', 'ab', 'abcde', 'xyz']) == ['ab', 'abcd']

def test_sorted_list_sum_with_non_string_elements():
    with pytest.raises(TypeError):
        sorted_list_sum([1, 2, 3, 4])

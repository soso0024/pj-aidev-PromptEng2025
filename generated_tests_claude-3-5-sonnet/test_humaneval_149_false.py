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

def test_basic_list():
    assert sorted_list_sum(['aa', 'bbbb', 'ccc']) == ['aa', 'bbbb']

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_no_even_length_strings():
    assert sorted_list_sum(['a', 'ccc', 'eeeee']) == []

def test_all_even_length_strings():
    assert sorted_list_sum(['aa', 'bbbb', 'cccc']) == ['aa', 'bbbb', 'cccc']

@pytest.mark.parametrize("input_list,expected", [
    (['aa', 'bbbb', 'cc', 'dddd'], ['aa', 'cc', 'bbbb', 'dddd']),
    (['', 'aa', 'bbbb'], ['', 'aa', 'bbbb']),
    (['zzzz', 'aa', 'bb'], ['aa', 'bb', 'zzzz']),
    (['a', 'bb', 'ccc', 'dddd'], ['bb', 'dddd'])
])
def test_various_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_special_characters():
    assert sorted_list_sum(['!!', '@@@@', '##']) == ['!!', '@@@@']

def test_numbers_as_strings():
    assert sorted_list_sum(['11', '2222', '333']) == ['11', '2222']

def test_mixed_case():
    assert sorted_list_sum(['AA', 'bbBB', 'CCc']) == ['AA', 'bbBB']

def test_whitespace():
    assert sorted_list_sum(['  ', '    ', ' ']) == ['  ', '    ']

def test_unicode_strings():
    assert sorted_list_sum(['αα', 'ββββ', 'γγγ']) == ['αα', 'ββββ']

@pytest.mark.parametrize("input_list", [
    None,
    42,
    "string",
    True,
    3.14
])
def test_invalid_input_type(input_list):
    with pytest.raises((AttributeError, TypeError)):
        sorted_list_sum(input_list)

def test_nested_lists():
    with pytest.raises(TypeError):
        sorted_list_sum([['aa'], ['bbbb']])

def test_list_with_non_strings():
    with pytest.raises(TypeError):
        sorted_list_sum(['aa', 42, 'bbbb'])
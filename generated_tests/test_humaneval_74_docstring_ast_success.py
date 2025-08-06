# Test cases for HumanEval/74
# Generated using Claude API


def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''

    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2


# Generated test cases:
import pytest

def test_empty_lists():
    assert total_match([], []) == []

def test_equal_length_lists():
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

def test_different_length_lists():
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

def test_single_element_lists():
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

@pytest.mark.parametrize("lst1, lst2, expected", [
    (["hello"], ["hi"], ["hi"]),
    (["a", "b", "c"], ["def"], ["a", "b", "c"]),
    (["test"], ["test"], ["test"]),
    (["python", "code"], ["py", "co"], ["py", "co"]),
    ([""], [""], [""]),
    (["a"], [""], [""]),
    ([""], ["a"], [""]),
    (["abc", "def"], ["abcdef"], ["abc", "def"]),
    (["long string here"], ["short"], ["short"]),
    (["a", "b", "c", "d"], ["abcd"], ["a", "b", "c", "d"])
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_lists_with_special_chars():
    assert total_match(["!@#", "$%^"], ["123", "456"]) == ["!@#", "$%^"]

def test_lists_with_spaces():
    assert total_match(["hello world"], ["hello", "world"]) == ["hello", "world"]

def test_lists_with_numbers():
    assert total_match(["123", "456"], ["1", "2", "3", "4"]) == ["1", "2", "3", "4"]

def test_unicode_strings():
    assert total_match(["über", "café"], ["cafe", "uber"]) == ["über", "café"]

def test_mixed_case_strings():
    assert total_match(["HELLO", "WORLD"], ["hello", "world"]) == ["HELLO", "WORLD"]

def test_lists_with_empty_strings():
    assert total_match(["", "test", ""], ["test", ""]) == ["", "test", ""]

def test_single_char_strings():
    assert total_match(["a", "b", "c"], ["d", "e"]) == ["d", "e"]

def test_identical_lists():
    test_list = ["same", "content"]
    assert total_match(test_list, test_list.copy()) == test_list
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

def total_match(lst1, lst2):
    l1 = sum(len(st) for st in lst1)
    l2 = sum(len(st) for st in lst2)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

def test_total_match_empty_lists():
    assert total_match([], []) == []

def test_total_match_single_element_lists():
    assert total_match(['hello'], ['world']) == ['hello']
    assert total_match(['world'], ['hello']) == ['world']

def test_total_match_different_length_lists():
    assert total_match(['hello', 'world'], ['foo']) == ['foo']
    assert total_match(['foo'], ['hello', 'world']) == ['hello', 'world']

def test_total_match_equal_length_lists():
    assert total_match(['hello', 'world'], ['foo', 'bar']) == ['hello', 'world']

def test_total_match_mixed_string_lengths():
    assert total_match(['hello', 'world', 'foo'], ['bar', 'baz']) == ['bar', 'baz']
    assert total_match(['bar', 'baz'], ['hello', 'world', 'foo']) == ['hello', 'world', 'foo']

def test_total_match_with_empty_strings():
    assert total_match(['hello', '', 'world'], ['foo', '', 'bar']) == ['hello', '', 'world']
    assert total_match(['foo', '', 'bar'], ['hello', '', 'world']) == ['foo', '', 'bar']

def test_total_match_with_none_input():
    with pytest.raises(TypeError):
        total_match(None, ['hello', 'world'])
    with pytest.raises(TypeError):
        total_match(['hello', 'world'], None)

def test_total_match_with_non_list_input():
    with pytest.raises(TypeError):
        total_match('hello', ['world'])
    with pytest.raises(TypeError):
        total_match(['hello'], 'world')
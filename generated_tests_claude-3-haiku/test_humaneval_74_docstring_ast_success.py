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

def test_total_match_empty_lists():
    assert total_match([], []) == []

def test_total_match_equal_length():
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

def test_total_match_lst1_shorter():
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

def test_total_match_lst2_shorter():
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

def test_total_match_single_element_lists():
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

def test_total_match_different_case():
    assert total_match(['HI', 'ADMIN'], ['hi', 'admin']) == ['HI', 'ADMIN']

def test_total_match_empty_lists_in_lists():
    assert total_match([[], []], [[], []]) == [[], []]

def test_total_match_mixed_string_lengths():
    assert total_match(['a', 'bb', 'ccc'], ['x', 'yy', 'zzz']) == ['a', 'bb', 'ccc']

def test_total_match_single_element_lists_equal_length():
    assert total_match(['abc'], ['def']) == ['abc']

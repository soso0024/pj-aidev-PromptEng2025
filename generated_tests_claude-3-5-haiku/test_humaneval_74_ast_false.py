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
        return lst1 if lst1 else lst2
    else:
        return lst2 if lst2 else lst1

def test_total_match_equal_length_lists():
    assert total_match(['a', 'b'], ['xx', 'yy']) == ['a', 'b']

def test_total_match_first_list_shorter():
    assert total_match(['a', 'bb'], ['xxx', 'yyyy']) == ['a', 'bb']

def test_total_match_second_list_shorter():
    assert total_match(['aaaa', 'bbb'], ['xx', 'y']) == ['xx', 'y']

def test_total_match_empty_lists():
    assert total_match([], []) == []

def test_total_match_first_list_empty():
    assert total_match([], ['a', 'b']) == ['a', 'b']

def test_total_match_second_list_empty():
    assert total_match(['a', 'b'], []) == ['a', 'b']

def test_total_match_single_element_lists():
    assert total_match(['hello'], ['world']) == ['hello']

@pytest.mark.parametrize("lst1,lst2,expected", [
    (['python'], ['code'], ['python']),
    (['a', 'b', 'c'], ['xx', 'yy', 'zz'], ['a', 'b', 'c']),
    (['long', 'longer'], ['short'], ['short']),
    (['', ''], ['', ''],['']),
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_unicode_strings():
    assert total_match(['こんにちは'], ['world']) == ['こんにちは']

def test_total_match_mixed_length_strings():
    assert total_match(['a', 'bcd', 'efg'], ['x', 'yz']) == ['x', 'yz']
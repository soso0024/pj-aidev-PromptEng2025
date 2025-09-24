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

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([], [], []),
    (['hi', 'admin'], ['hI', 'Hi'], ['hI', 'Hi']),
    (['hi', 'admin'], ['hi', 'hi', 'admin', 'project'], ['hi', 'admin']),
    (['hi', 'admin'], ['hI', 'hi', 'hi'], ['hI', 'hi', 'hi']),
    (['4'], ['1', '2', '3', '4', '5'], ['4']),
    (['a'], ['b'], ['a']),
    (['ab'], ['cd'], ['ab']),
    (['abc'], ['de'], ['de']),
    (['hello'], ['world'], ['hello']),
    ([''], [''], ['']),
    (['', ''], [''], ['', '']),
    (['a', 'b'], ['c'], ['c']),
    (['aa'], ['b', 'c'], ['aa']),
    (['test'], ['a', 'b', 'c', 'd'], ['test']),
    (['long string here'], ['a', 'b', 'c'], ['a', 'b', 'c']),
    (['x', 'y', 'z'], ['abc'], ['x', 'y', 'z']),
    ([''], ['a'], ['']),
    (['a'], [''], ['']),
    ([], ['a'], []),
    (['a'], [], []),
    (['same'], ['same'], ['same']),
    (['ab', 'cd'], ['ef', 'gh'], ['ab', 'cd']),
    (['python', 'code'], ['test', 'case', 'here'], ['python', 'code']),
    (['very long string'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
])
def test_total_match(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_empty_lists():
    assert total_match([], []) == []

def test_total_match_one_empty():
    assert total_match([], ['a']) == []
    assert total_match(['a'], []) == []

def test_total_match_equal_length():
    result = total_match(['ab'], ['cd'])
    assert result == ['ab']

def test_total_match_single_chars():
    assert total_match(['a'], ['b']) == ['a']

def test_total_match_empty_strings():
    assert total_match([''], ['']) == ['']
    assert total_match(['', ''], ['']) == ['', '']

def test_total_match_mixed_lengths():
    assert total_match(['a', 'bb', 'ccc'], ['dddd']) == ['dddd']
    assert total_match(['aaaaa'], ['b', 'cc', 'ddd']) == ['aaaaa']
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

def test_total_match_basic():
    assert total_match(['abc', 'def'], ['gh', 'ij']) == ['gh', 'ij']
    assert total_match(['a', 'b'], ['abc']) == ['a', 'b']

@pytest.mark.parametrize("lst1, lst2, expected", [
    ([], [], []),
    ([''], [''], ['']),
    (['a'], ['b'], ['a']),
    (['abc'], ['def'], ['abc']),
    (['hello', 'world'], ['hi'], ['hi']),
    (['a', 'b', 'c'], ['def', 'ghi'], ['a', 'b', 'c']),
    (['python'], ['py', 'thon'], ['python']),
    (['test'], ['t', 'e', 's', 't'], ['test']),
    (['abc', 'def', 'ghi'], ['abcdefghi'], ['abc', 'def', 'ghi']),
    (['   '], [' '], [' ']),
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_equal_lengths():
    assert total_match(['abc'], ['def']) == ['abc']
    assert total_match(['a', 'b'], ['cd']) == ['a', 'b']

def test_total_match_empty_strings():
    assert total_match([''], ['']) == ['']
    assert total_match(['', ''], ['']) == ['', '']

def test_total_match_special_characters():
    assert total_match(['!@#'], ['$%^']) == ['!@#']
    assert total_match(['⭐️', '🌟'], ['★']) == ['★']

def test_total_match_whitespace():
    assert total_match([' ', '  '], ['   ']) == [' ', '  ']
    assert total_match(['\n', '\t'], ['  ']) == ['\n', '\t']

def test_total_match_mixed_content():
    assert total_match(['abc123', 'def456'], ['xyz789']) == ['xyz789']
    assert total_match(['12', '34'], ['123', '4']) == ['12', '34']
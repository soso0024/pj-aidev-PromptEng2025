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

def test_total_match_empty_lists():
    assert total_match([], []) == []

def test_total_match_first_list_shorter():
    assert total_match(['a', 'bb'], ['ccc', 'd']) == ['a', 'bb']

def test_total_match_second_list_shorter():
    assert total_match(['abc', 'd'], ['e', 'ff']) == ['e', 'ff']

def test_total_match_lists_equal_length():
    assert total_match(['a', 'bb'], ['cc', 'd']) == ['a', 'bb']

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([], ['a', 'bb'], ['a', 'bb']),
    (['a', 'bb'], [], ['a', 'bb']),
    (['a', 'bb'], ['c', 'd'], ['a', 'bb']),
    (['abc', 'd'], ['e', 'ff'], ['e', 'ff'])
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_with_empty_strings():
    assert total_match(['a', '', 'bb'], ['a', 'd', '']) == ['a', '', 'bb']

def test_total_match_with_none_values():
    with pytest.raises(TypeError):
        total_match(['a', None, 'bb'], ['a', 'd', None])
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

def test_total_match_first_list_longer():
    assert total_match(['hello', 'world'], ['hi']) == ['hello', 'world']

def test_total_match_second_list_longer():
    assert total_match(['hi'], ['hello', 'world']) == ['hello', 'world']

def test_total_match_equal_length():
    assert total_match(['hello'], ['world']) == ['world']

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([], ['a', 'b', 'c'], ['a', 'b', 'c']),
    (['x', 'y'], [], ['x', 'y']),
    (['a', 'b'], ['c', 'd'], ['c', 'd']),
    (['hello', 'world'], ['hi', 'there'], ['hi', 'there'])
])
def test_total_match_various_inputs(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_with_empty_strings():
    assert total_match(['', 'hello', ''], ['world', '', 'test']) == ['world', '', 'test']

def test_total_match_with_none_values():
    with pytest.raises(TypeError):
        total_match(['hello', None, 'world'], ['hi', 'there'])

def test_total_match_with_non_string_values():
    with pytest.raises(TypeError):
        total_match(['hello', 123, 'world'], ['hi', 'there'])
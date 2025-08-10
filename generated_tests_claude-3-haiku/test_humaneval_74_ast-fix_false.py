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

def test_total_match_one_empty_list():
    assert total_match([], ['hello', 'world']) == []
    assert total_match(['hello', 'world'], []) == ['hello', 'world']

@pytest.mark.parametrize("lst1,lst2,expected", [
    (['hello'], ['world'], ['hello']),
    (['hello', 'world'], ['hi'], ['hello', 'world']),
    (['a', 'bb', 'ccc'], ['x', 'yy'], ['a', 'bb', 'ccc']),
    (['aaa', 'b', 'cc'], ['d', 'ee', 'fff'], ['d', 'ee', 'fff'])
])
def test_total_match_normal_cases(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_equal_length():
    assert total_match(['a', 'bb'], ['x', 'yy']) == ['a', 'bb']
    assert total_match(['aaa', 'b'], ['d', 'ee']) == ['d', 'ee']

def test_total_match_single_element_lists():
    assert total_match(['hello'], ['world']) == ['hello']
    assert total_match(['world'], ['hello']) == ['world']

def test_total_match_with_none():
    with pytest.raises(TypeError):
        total_match(None, ['hello', 'world'])
    with pytest.raises(TypeError):
        total_match(['hello', 'world'], None)

def total_match(lst1, lst2):
    l1 = sum(len(s) for s in lst1)
    l2 = sum(len(s) for s in lst2)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2
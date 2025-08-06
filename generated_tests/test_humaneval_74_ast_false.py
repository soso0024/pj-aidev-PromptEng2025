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

def test_total_match_equal_length():
    assert total_match(["abc", "def"], ["ghi", "jkl"]) == ["abc", "def"]

def test_total_match_first_shorter():
    assert total_match(["a", "b"], ["abc", "def"]) == ["a", "b"]

def test_total_match_second_shorter():
    assert total_match(["abc", "def"], ["a", "b"]) == ["a", "b"]

@pytest.mark.parametrize("lst1, lst2, expected", [
    ([], [], []),
    ([""], [""], [""]),
    (["a"], ["b"], ["a"]),
    (["abc", "def", "ghi"], ["12", "345", "6789"], ["12", "345", "6789"]),
    (["hello", "world"], ["hi", "there"], ["hi", "there"]),
    (["x"], ["xx"], ["x"]),
    (["long string"], ["short"], ["short"]),
    (["a", "b", "c"], ["def"], ["def"]),
    (["test"], ["t", "e", "s", "t"], ["test"])
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_empty_and_nonempty():
    assert total_match([], ["a", "b"]) == []
    assert total_match(["a", "b"], []) == []

def test_total_match_single_empty_string():
    assert total_match([""], ["a"]) == [""]
    assert total_match(["a"], [""]) == [""]

def test_total_match_same_total_length():
    assert total_match(["ab", "cd"], ["abcd"]) == ["ab", "cd"]
    assert total_match(["abcd"], ["ab", "cd"]) == ["abcd"]

@pytest.mark.parametrize("lst1, lst2, expected", [
    (["hello world"], ["hello", "world"], ["hello", "world"]),
    (["a", "b", "c", "d"], ["abcd"], ["a", "b", "c", "d"]),
    (["12345"], ["1", "2", "3", "4", "5"], ["12345"])
])
def test_total_match_different_splits(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected
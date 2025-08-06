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

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([], [], []),
    (["hi", "admin"], ["hI", "Hi"], ["hI", "Hi"]),
    (["hi", "admin"], ["hi", "hi", "admin", "project"], ["hi", "admin"]),
    (["hi", "admin"], ["hI", "hi", "hi"], ["hI", "hi", "hi"]),
    (["4"], ["1", "2", "3", "4", "5"], ["4"]),
    (["hello"], ["hi"], ["hi"]),
    (["a", "b", "c"], ["aa", "bb"], ["a", "b", "c"]),
    (["test"], ["test"], ["test"]),
    (["python", "code"], ["py", "c"], ["py", "c"]),
    ([""], [""], [""]),
    (["a"], [""], [""]),
    (["abc", "def"], ["abcdef"], ["abc", "def"]),
    (["   "], ["a"], ["a"]),
    (["!@#"], ["123"], ["!@#"]),
    (["long string here"], ["short"], ["short"])
])
def test_total_match_parametrized(lst1, lst2, expected):
    assert total_match(lst1, lst2) == expected

def test_total_match_identical_lists():
    assert total_match(["same", "list"], ["same", "list"]) == ["same", "list"]

def test_total_match_empty_and_nonempty():
    assert total_match([], ["nonempty"]) == []

def test_total_match_special_chars():
    assert total_match(["@#$", "%%%"], ["!!!"]) == ["!!!"]

def test_total_match_whitespace():
    assert total_match(["  ", "    "], [" "]) == [" "]

def test_total_match_same_total_length():
    assert total_match(["ab", "cd"], ["abcd"]) == ["ab", "cd"]

def test_total_match_unicode():
    assert total_match(["é", "ñ"], ["a", "b"]) == ["é", "ñ"]

def test_total_match_single_char_lists():
    assert total_match(["a"], ["b"]) == ["a"]

def test_total_match_mixed_lengths():
    assert total_match(["short", "strings"], ["one", "very", "long", "string"]) == ["short", "strings"]
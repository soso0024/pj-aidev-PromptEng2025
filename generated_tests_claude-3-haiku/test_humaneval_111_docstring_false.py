# Test cases for HumanEval/111
# Generated using Claude API


def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    dict1={}
    list1=test.split(" ")
    t=0

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1


# Generated test cases:
from collections import Counter
import pytest
from solution import histogram

@pytest.mark.parametrize("input,expected", [
    ("a b c", {'a': 1, 'b': 1, 'c': 1}),
    ("a b b a", {'a': 2, 'b': 2}),
    ("a b c a b", {'a': 2, 'b': 2}),
    ("b b b b a", {'b': 4}),
    ("", {}),
    ("   ", {}),
    ("a a a a a", {'a': 5}),
    ("a b c d e", {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}),
    ("a a a b b b", {'a': 3, 'b': 3}),
    ("a b c a b c", {'a': 2, 'b': 2, 'c': 2}),
])
def test_histogram(input, expected):
    assert histogram(input) == expected

def test_empty_string():
    assert histogram("") == {}

def test_all_whitespace():
    assert histogram("   ") == {}

def test_single_character():
    assert histogram("a") == {'a': 1}

def test_duplicate_characters():
    assert histogram("a a a a a") == {'a': 5}

def test_multiple_unique_characters():
    assert histogram("a b c d e") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

def test_multiple_duplicate_characters():
    assert histogram("a a a b b b") == {'a': 3, 'b': 3}

def test_equal_duplicate_characters():
    assert histogram("a b c a b c") == {'a': 2, 'b': 2, 'c': 2}
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
import pytest

def histogram(test):
    dict1 = {}
    list1 = test.split()
    t = 0

    for i in list1:
        if list1.count(i) > t:
            t = list1.count(i)
    
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    
    return dict1

def test_histogram_normal_case():
    assert histogram("apple banana apple orange banana") == {"apple": 2, "banana": 2}

def test_histogram_single_word():
    assert histogram("hello") == {"hello": 1}

def test_histogram_empty_string():
    assert histogram("") == {}

def test_histogram_multiple_max_frequency_words():
    assert histogram("cat dog cat dog") == {"cat": 2, "dog": 2}

def test_histogram_case_sensitive():
    assert histogram("Apple apple APPLE") == {"Apple": 1, "apple": 1, "APPLE": 1}

def test_histogram_with_spaces():
    assert histogram("  hello   world  hello  ") == {"hello": 2}

def test_histogram_with_special_characters():
    assert histogram("hello! world! hello!") == {"hello!": 2, "world!": 1}

def test_histogram_with_numbers():
    assert histogram("1 2 3 1 2 1") == {"1": 3}

@pytest.mark.parametrize("input_str,expected", [
    ("apple banana apple orange banana", {"apple": 2, "banana": 2}),
    ("hello", {"hello": 1}),
    ("", {}),
    ("cat dog cat dog", {"cat": 2, "dog": 2}),
    ("  hello   world  hello  ", {"hello": 2}),
    ("1 2 3 1 2 1", {"1": 3}),
    ("hello! world! hello!", {"hello!": 2, "world!": 1})
])
def test_histogram_parametrized(input_str, expected):
    assert histogram(input_str) == expected
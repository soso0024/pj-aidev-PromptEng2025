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

def test_histogram_basic_case():
    assert histogram("apple banana apple cherry") == {"apple": 2}

def test_histogram_multiple_max_frequency():
    assert histogram("apple banana apple banana") == {"apple": 2, "banana": 2}

def test_histogram_empty_string():
    assert histogram("") == {}

def test_histogram_single_word():
    assert histogram("hello") == {"hello": 1}

def test_histogram_all_unique_words():
    assert histogram("one two three four") == {}

def test_histogram_with_extra_spaces():
    assert histogram("  apple   banana   apple  ") == {"apple": 2}

def test_histogram_case_sensitive():
    assert histogram("Apple apple APPLE") == {"Apple": 1, "apple": 1, "APPLE": 1}

@pytest.mark.parametrize("input_string,expected", [
    ("red blue red green red", {"red": 3}),
    ("cat dog cat bird cat dog", {"cat": 3, "dog": 2}),
    ("a b c d e f", {}),
    ("hello hello hello", {"hello": 3})
])
def test_histogram_parametrized(input_string, expected):
    assert histogram(input_string) == expected